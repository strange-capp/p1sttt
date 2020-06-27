from app import create_all
from app import db
from app.models import Record

app = create_all('default')
app.app_context().push()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Record=Record, current_app=app)
