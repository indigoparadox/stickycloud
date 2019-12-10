
import logging
from flask import current_app, render_template, abort, jsonify, request
from . import db
from .models import Note, Tag
from .forms import NoteForm
from datetime import datetime

@current_app.route( '/notes/new', methods=['POST'] )
def stickycloud_note_new():

    form = NoteForm( request.form )
    if form.validate_on_submit():
        content = form.content
        note = Note( title=form.title, content=content, created=datetime.now(),
            modified=datetime.now(), color=0 )
        db.session.add( note )
        db.session.commit()

@current_app.route( '/notes/<int:note_id>' )
def stickycloud_note( note_id ):
    # TODO: Check owner vs currently logged in.

    query = db.Query( 'Note' ) \
        .filter( Note.id == note_id )
    note = query.first()

    if not note:
        abort( 404 )

    return jsonify( note )

@current_app.route( '/' )
def stickycloud_root():
    return render_template( 'root.html' )

