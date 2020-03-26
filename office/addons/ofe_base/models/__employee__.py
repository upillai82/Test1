class Employee(models.Model):
    _name = "ofe.employee"
    _inherit = 'image.mixin'
    _description = "Employee"
    
    name = fields.Char(string="First Name",required=True)
    last_name = fields.Char(string="Last Name")
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],string="Gender")
    dob = fields.Date(string="Date of Birth")
    height = fields.Float(string="height")
    age = fields.Integer(string="Age")
    admitted_date = fields.Datetime(string="Admitted Date and time")
    remarks = fields.Text(string="Remarks")
    description = fields.Html(string="Description")
    department_id = fields.Many2one('ofe.department',string="Department",ondelete="set null")
    language_ids = fields.Many2many('ofe.language',string="Languages known")
    education_ids = fields.One2many('ofe.education','student_id',string="Education Details",help="Previous Education Details")
    attachment_ids = fields.Many2many('ir.attachment',string="Attachment")