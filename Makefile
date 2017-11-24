help:
    @sphinx-build -M help "docs/" "_docs/"

clean:
    -rm -fr _docs/

documentation:
    @sphinx-build -b singlehtml docs/ _docs/

graph:
    @python manage.py graph_models database

urls:
    @python manage.py show_urls
