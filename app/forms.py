from wtforms import Form, StringField, validators, TextAreaField
from flask_ckeditor import CKEditorField

class EmailForm(Form):
  fromField = StringField(u'From:', validators=[validators.input_required()])
  toField  = StringField(u'To:', validators=[validators.optional()])
  ccField  = StringField(u'CC:', validators=[validators.optional()])
  subjectField  = StringField(u'Subject:', validators=[validators.optional()])
  messageField  = CKEditorField(u'Message:')

  def __init__(self, defaultData):
    super(EmailForm, self).__init__()
    self.fromField.data = defaultData["from"]
    self.toField.data = defaultData["to"]
    self.ccField.data = defaultData["cc"]
    self.subjectField.data = defaultData["subject"]
    self.messageField = defaultData["message"]
