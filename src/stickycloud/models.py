
from . import db

class User( db.Model ):

    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key=True )
    email = db.Column(
        db.String( 128 ), index=True, unique=True, nullable=False )
    stored_key = db.Column( db.Text, index=False, unique=False, nullable=False )
    created = db.Column(
        db.DateTime, index=False, unique=False, nullable=False )
    tags = db.relationship( 'Tag', back_populates='owner' )
    attachments = db.relationship( 'Attachment', back_populates='owner' )
    notes = db.relationship( 'Note', back_populates='owner' )

notes_tags = db.Table( 'notes_tags', db.metadata,
    db.Column( 'notes_id', db.Integer, db.ForeignKey( 'notes.id' ) ),
    db.Column( 'tags_id', db.Integer, db.ForeignKey( 'tags.id' ) ) )

class Tag( db.Model ):

    __tablename__ = 'tags'

    id = db.Column( db.Integer, primary_key=True )
    parent_id = db.Column(
        db.Integer, db.ForeignKey( 'tags.id' ), nullable=True )
    parent = db.relationship( 'Tag', remote_side=[id] )
    #tag_parent = db.relationship( 'Tag', remote_side=[id] )
    display_name = db.Column(
        db.String( 64 ), index=True, unique=False, nullable=False )
    owner = db.relationship( 'User', back_populates='tags' )
    owner_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    note_id = db.Column( db.Integer, db.ForeignKey( 'notes.id' ) )
    notes = db.relationship(
        'Note', secondary=notes_tags, back_populates='tags' )
    children = db.relationship( 'Tag', backref=db.backref(
        'tag_parent', remote_side=[id] ) )

class Note( db.Model ):

    __tablename__ = 'notes'

    id = db.Column( db.Integer, primary_key=True )
    title = db.Column(
        db.String( 256 ), index=True, unique=False, nullable=False )
    content = db.Column( db.Text, index=False, unique=False, nullable=False )
    color = db.Column( db.Integer, index=False, unique=False, nullable=False )
    created = db.Column( db.DateTime, index=True, unique=False, nullable=False )
    modified = \
        db.Column( db.DateTime, index=True, unique=False, nullable=False )
    owner = db.relationship( 'User', back_populates='notes' )
    owner_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    
class Attachments( db.Model ):

    __tablename__ = 'attachments'

    id = db.Column( db.Integer, primary_key=True )
    owner = db.relationship( 'User', back_populates='attachments' )
    owner_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    name = \
        db.Column( db.String( 256 ), index=True, unique=False, nullable=False )
    content = db.Column( db.Binary, index=False )
    created = db.Column( db.DateTime, index=True, unique=False, nullable=False )
    modified = \
        db.Column( db.DateTime, index=True, unique=False, nullable=False )
