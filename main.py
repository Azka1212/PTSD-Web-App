from website import create_app

app = create_app()

# line inplace to run only when called
if __name__ == '__main__':
    # debug = True    -- to automatically rerun server when changes are made
    app.run(debug=True)
    