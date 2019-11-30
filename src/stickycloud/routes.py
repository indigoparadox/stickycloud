
import logging
from .database import db_session

@current_app.teardown_appcontext
def shutdown_session( exception=None ):
    db_session.remove()

@app.route( '/' )
def stickycloud_root():
    return render_template( 'root.html' )

