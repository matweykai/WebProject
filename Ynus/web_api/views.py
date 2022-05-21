from rest_framework.views import APIView
from django.contrib.auth.models import User
from website.models import Discipline, Direction, Vote
from rest_framework import status
from rest_framework.response import Response


class VotesView(APIView):
    """API view for working with votes"""
    def post(self, *args, **kwargs):
        """Add company's vote for some discipline in the direction"""
        try:
            user = self.request.user

            direction_id = self.request.data.get('direction_id')
            discipline_name = self.request.data.get('discipline_name')

            direction = Direction.objects.get(pk=direction_id)
            discipline = Discipline.objects.get(name=discipline_name)
            company = user.company

            Vote.objects.create(company=company, discipline=discipline, direction=direction)

            return Response(status=status.HTTP_200_OK)

        except (Direction.DoesNotExist, Discipline.DoesNotExist,
                User.company.RelatedObjectDoesNotExist) as ex:
            print(ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        """Deletes company's vote for the discipline"""
        try:
            user = self.request.user

            direction_id = self.request.data.get('direction_id')
            discipline_name = self.request.data.get('discipline_name')

            direction = Direction.objects.get(pk=direction_id)
            discipline = Discipline.objects.get(name=discipline_name)
            company = user.company

            vote = Vote.objects.get(company=company, discipline=discipline, direction=direction)
            vote.delete()

            return Response(status=status.HTTP_200_OK)

        except (Direction.DoesNotExist, Discipline.DoesNotExist,
                User.company.RelatedObjectDoesNotExist, Vote.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, *args, **kwargs):
        """Returns percent statistics for every discipline in the direction"""
        try:
            direction_id = self.request.query_params.get('pk')
            #print(direction_id)

            direction = Direction.objects.get(pk=direction_id)

            content = []

            all_voted_companies = list()
            # Counting all votes in this direction
            for vote in direction.vote_set.all():
                all_voted_companies.append(vote.company.user.username)

            unique_votes_count = len(set(all_voted_companies))

            for discipline in direction.disciplines.all():

                content.append({
                    "id": discipline.id,
                    "percents": int((len(discipline.vote_set.all()) / unique_votes_count
                    if unique_votes_count != 0 else 0) * 100)
                })

            return Response(content, status=status.HTTP_200_OK)

        except (Direction.DoesNotExist, Discipline.DoesNotExist) as ex:
            print(ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VotedCompaniesView(APIView):
    """API view for getting lists of companies that voted in some direction"""
    def get(self, *args, **kwargs):
        try:
            direction_id = self.request.query_params.get('pk')

            direction = Direction.objects.get(pk=direction_id)

            content = []

            for discipline in direction.disciplines.all():
                content.append({
                    "id": discipline.id,
                    "companies_name": [vote.company.user.username for vote in discipline.vote_set.all()]
                })

            #print(content)
            return Response(content, status=status.HTTP_200_OK)

        except (Direction.DoesNotExist, Discipline.DoesNotExist) as ex:
            print(ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)

