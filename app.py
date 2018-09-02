import os
import app


if __name__ == '__main__':
    app_host = os.environ.get('HOST', '0.0.0.0')
    app_port = int(os.environ.get('PORT', 5000))
    system = app.System()
    system.run(host=app_host, port=app_port)
