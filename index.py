import os
import sys
import traceback
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Django application
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'research_journal.settings')
    application = get_wsgi_application()
    logger.info("Django application initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Django application: {str(e)}")
    raise

def handler(request):
    try:
        logger.info(f"Received request: {request}")
        
        # Get the request path
        path = request.get('path', '/')
        logger.info(f"Processing request path: {path}")
        
        # Create WSGI environment
        environ = {
            'REQUEST_METHOD': request.get('method', 'GET'),
            'PATH_INFO': path,
            'QUERY_STRING': request.get('query', ''),
            'wsgi.input': request.get('body', ''),
            'wsgi.url_scheme': 'https',
            'HTTP_HOST': request.get('headers', {}).get('host', ''),
            'HTTP_ACCEPT': 'application/json',
            'SERVER_NAME': 'localhost',
            'SERVER_PORT': '80',
            'CONTENT_TYPE': request.get('headers', {}).get('content-type', 'application/json'),
            'CONTENT_LENGTH': str(len(request.get('body', ''))) if request.get('body') else '0'
        }
        
        # Add all headers to environ
        for key, value in request.get('headers', {}).items():
            environ[f'HTTP_{key.upper().replace("-", "_")}'.replace(" ", "_")] = value
        
        logger.info(f"WSGI environment created: {environ}")
        
        # Process request through Django
        from django.core.handlers.wsgi import WSGIHandler
        wsgi_handler = WSGIHandler()
        response = wsgi_handler(environ, lambda status, headers: None)
        
        logger.info("Django request processed successfully")
        
        # Convert Django response to Vercel response
        status_code = response.status_code
        headers = dict(response.items())
        content = response.content
        
        logger.info(f"Response status: {status_code}")
        logger.info(f"Response headers: {headers}")
        
        return {
            'statusCode': status_code,
            'headers': headers,
            'body': content.decode('utf-8') if content else ''
        }
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        logger.error(traceback.format_exc())
        return {
            'statusCode': 500,
            'body': f"Internal Server Error: {str(e)}"
        }
