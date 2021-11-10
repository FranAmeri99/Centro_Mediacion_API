from django.test import TestCase
from core.models import State, Case, MediationPortafolio, MediationSessions
from Users.models import User
from Resolution.models import Resolution

from django.utils.timezone import now

class ModelTests(TestCase):

    def test_State(self):
        """Test Create State """
        description = 'Una descripcion'
        state = State.objects.create(
            description = description
            )
        self.assertEqual(state.description, description)
    
    def test_case(self):
        """Create case"""
        mediator = User.objects.create_mediator(
            'test1@superuser.com', 
            'test1',
            '1111'
            )
        lawyer_applicant = User.objects.create_lawyer_user(
            'test2@hgj.com', 
            'test2',
            '22222'
            )
        lawyer_defendant = User.objects.create_lawyer_user(
            'test3@ert.com', 
            'test3',
            '3333'
            )
        client_applicant = User.objects.create_user(
            'test4@qwe.com', 
            'test4'
            )
        client_defendant = User.objects.create_user(
            'test5@asd.com', 
            'test5'
            )
        mediator.save()
        lawyer_applicant.save()
        lawyer_defendant.save()
        client_applicant.save()
        client_defendant.save()
        name = 'Ford vs Ferrari'
        case = Case.objects.create(
            name=name,
            mediator = mediator,
            lawyer_applicant = lawyer_applicant,
            lawyer_defendant = lawyer_defendant,
            client_applicant = client_applicant,
            client_defendant = client_defendant   
        )
        state = State.objects.create(
            description = "una description"
            )
        case.save()
        
        portfolio = MediationPortafolio.objects.create(
            start_date = now(),
            end_date = now(),
            state = state,
            resolution = Resolution.objects.create(description = 'no se resolvio'),
            case = case
        )
        self.assertEqual(portfolio.case.client_defendant, case.client_defendant)
        
        self.assertEqual(case.mediator.email, mediator.email)
        self.assertEqual(case.lawyer_applicant.email, lawyer_applicant.email)
        self.assertEqual(case.lawyer_defendant.email, lawyer_defendant.email)
        