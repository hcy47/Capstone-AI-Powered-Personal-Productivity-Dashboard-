class DevelopmentConfig():
  SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
  DEBUG = True
  # CACHE_TYPE = 'SimpleCache'

  class ProductionConfig():
    pass