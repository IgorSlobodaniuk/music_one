
from education.models import CardOrdering
from education.models.user_education_status import UserEducationStatus
from education.models.quest_structure import (
    LEVEL_EXAM,
    GROUP_TEST,
    QUEST,
)
from education.models.quest_structure import (
    LevelExam,
    GroupTest,
    Quest,
)

CARD_OBJ = {
    LEVEL_EXAM: LevelExam,
    GROUP_TEST: GroupTest,
    QUEST: Quest
}


class EducationService:

    def get_current_card_id(self, user):
        try:
            current_card_order_id = UserEducationStatus.objects.get(user=user).current_card
        except UserEducationStatus.DoesNotExist:
            current_card_order_id = 1
        return CardOrdering.objects.get(pk=current_card_order_id).pk

    def get_all_questions_by_card(self, card_id, card_type):
        data = []
        obj = CARD_OBJ.get(card_type)
        card_questions = obj.objects.get(pk=card_id).questions.all()
        for question in card_questions:
            answer_variants = question.answer_variants.values('pk', 'name')
            data.append({
                'id': question.pk,
                'name': question.name,
                'answer_variants': answer_variants
            })

        return data

    def test_checker(self, data, user):
        mark = 0
        data_results = data['results']
        card_type = data['card_type']
        card_id = data['card_id']
        questions = CARD_OBJ.get(card_type).objects.get(pk=card_id).questions.all()
        for question_id, answer_id in data_results.items():
            question = questions.get(pk=question_id)
            correct_answer_id = question.answer_variants.get(is_correct=True).pk
            if correct_answer_id == answer_id:
                mark += 1

        return {
            'user': user,
            'card': card_id,
            'mark': mark
        }
