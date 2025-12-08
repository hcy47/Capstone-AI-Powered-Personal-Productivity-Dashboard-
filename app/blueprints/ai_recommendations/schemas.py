from app.extensions import ma
from app.models import Ai_recommendation

class AiRecommendationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ai_recommendation
        include_fk = True

ai_recommendation_schema = AiRecommendationSchema()
ai_recommendations_schema = AiRecommendationSchema(many=True)
