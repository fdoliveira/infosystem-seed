from app import application

if __name__ == '__main__':
    application.load_app().run(debug=True, host='0.0.0.0', port=5000) 
