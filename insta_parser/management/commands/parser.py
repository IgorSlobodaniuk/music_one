import json
import os
from collections import defaultdict
from random import randint
from time import sleep
from typing import AnyStr, List, DefaultDict

import requests
from django.core.management.base import BaseCommand
from seleniumwire.webdriver import Chrome


class Command(BaseCommand):

    @staticmethod
    def sign_in(username, password, driver):
        driver.get('https://www.instagram.com/')
        sleep(randint(2, 4))
        driver.find_element_by_css_selector('input[name=username]').send_keys(username)
        sleep(randint(2, 4))
        driver.find_element_by_css_selector('input[name=password]').send_keys(password)
        sleep(randint(2, 4))
        driver.find_element_by_css_selector('button[type=submit]').click()
        sleep(randint(3, 7))

    @staticmethod
    def get_input_data():
        user_data = requests.get(f"{os.environ['PROJECT_URL']}/instagram_data")
        return {
            'highlights': [],
            'users': ['https://www.instagram.com/alexmusic12321/'],
            'igtv_hashtags': [],
            'highlight_hashtags': [],
        }

    def parse(self, username, password):
        driver = Chrome()
        self.sign_in(username, password, driver)
        input_data = self.get_input_data()
        output_data = dict()
        for user in input_data['users']:
            parse_user_data = {}
            driver.get(user)
            request = driver.wait_for_request('include_suggested_users')
            parse_user_data['highlights'] = self.get_highlights(
                driver,
                request,
                input_data['highlights'],
                input_data['highlight_hashtags'],
            )
            parse_user_data['igtvs'] = self.get_igtv_data(
                driver,
                user,
                input_data['igtv_hashtags'],
            )
            output_data[user] = parse_user_data
        self.send_to_app(output_data)

    @staticmethod
    def get_highlights(driver: Chrome, request: AnyStr, highlights: List, hashtags: List) -> DefaultDict:
        """
        :param driver: browser
        :param request: driver request
        :param highlights: list of highlights names
        :param hashtags: list of hashtags names
        :return: defaultdict
        """
        current_user_data = requests.get(request.url, headers=request.headers).text
        edges = json.loads(current_user_data)['data']['user']['edge_highlight_reels']['edges']
        items = defaultdict(list)
        for edge in edges:
            node = edge['node']
            title = node['title']
            if title not in highlights:
                continue

            driver.get('https://www.instagram.com/stories/highlights/{}'.format(node['id']))
            sleep(randint(2, 4))
            request = driver.wait_for_request('show_story_viewer_list')
            response_data = json.loads(requests.get(request.url, headers=request.headers).text)
            for item in response_data['data']['reels_media'][0]['items']:
                video_resources = item.get('video_resources')
                tappable_objects = item['tappable_objects']
                if tappable_objects and tappable_objects[0]['__typename'] == 'GraphTappableHashtag':
                    hashtag = tappable_objects[0]['name']
                    if hashtag not in hashtags:
                        continue

                    stories_data = {'story_id': node['id']}
                    if video_resources:
                        stories_data['story_url'] = video_resources[-1]['src']
                    items[hashtag].append(stories_data)
        return items

    @staticmethod
    def get_igtv_data(driver, user, hashtags):
        driver.get(f'{user}channel/')
        sleep(randint(3, 6))
        items = {}
        for item in driver.find_elements_by_css_selector('a._bz0w'):
            tag = item.find_element_by_css_selector('._2XLe_')
            if tag:
                hashtag = tag.text
                if hashtag not in hashtags:
                    continue

                items[hashtag.text] = tag.get_attribute('href')
        return items

    @staticmethod
    def send_to_app(output_data):
        requests.post(f"{os.environ['PROJECT_URL']}/instagram_data", json=output_data)
