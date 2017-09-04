""" run.py """
import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # pylint: disable=invalid-name
    app.run('', port=port)
    