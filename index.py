import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'research_journal.settings')
application = get_wsgi_application()

from django.http import JsonResponse

def handler(request):
    try:
        # Initialize Django application
        application = get_wsgi_application()
        
        # Get the request path
        path = request.get('path', '/')
        
        # Create a Django request object
        from django.core.handlers.wsgi import WSGIRequest
        from django.http import HttpRequest
        
        environ = {
            'REQUEST_METHOD': request.get('method', 'GET'),
            'PATH_INFO': path,
            'QUERY_STRING': request.get('query', ''),
            'wsgi.input': request.get('body', ''),
            'wsgi.url_scheme': 'https',
            'HTTP_HOST': request.get('headers', {}).get('host', ''),
            'HTTP_ACCEPT': 'application/json',
        }
        
        django_request = WSGIRequest(environ)
        
        # Get response from Django
        response = application(django_request)
        
        # Convert Django response to Vercel response
        status_code = response.status_code
        headers = dict(response.items())
        content = response.content
        
        return {
            'statusCode': status_code,
            'headers': headers,
            'body': content.decode('utf-8')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
