from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run()  # Or whatever command starts your app or gRPC server
