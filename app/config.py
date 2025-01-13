class Configuration():
    # autenticação com o banco de dados
    SQLALCHEMY_DATABASE_URI = "postgresql://admin_damiani:W3UV4UhL69S0BpY@db:5432/defense1_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Informações para autenticação das APIs do securiti
    # Informações para autenticação das APIs do securiti
    API_URL = "https://app.securiti.ai/reporting/v1/sources/multi_query?ref=getMetaDataForFilters"
    API_KEY = "mJi0Elmp5cxIBjYwu724QE6gJzsk0Unbow892lZj"
    API_SECRET = "l38x7E7qlPiDm6Di81YMb68JfDFVDEu5NuEkJFEW"
    API_TIDENT = "e84f4560-55b1-4157-80d2-5fd77368dd24"
    API_CONTENT_TYPE = "application/json"
    API_COOKIE = "_xsrf=bzh5U1hHMTAzZzdHTmpsT0tUdkdRb2ZMZE0xa3RIM2I=|1735320209728039019|86c653b9e1fd97187d0e1c7fe0b759c6c916e312"