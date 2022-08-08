from datetime import date, datetime
from distutils.command.upload import upload
from email.policy import default
from ssl import create_default_context
from tabnanny import verbose
from tokenize import blank_re
from django.db import models
from django.utils import timezone
# Create your models here.
class KDS(models.Model):
    link = models.CharField(default='Edit', max_length=100)
    already_mapped=models.CharField(verbose_name='Already Mapped', blank=True, max_length=100, null=True)
    
    #master_name_choices = [('CM', 'Customer Master'),('MM', 'Material Master'),('REFX', 'Real Estate Master')]
    master_name=models.CharField(verbose_name='Master Name', blank=True, max_length=100, null=True)
    
    section=models.CharField(verbose_name='Section', blank=True, max_length=100, null=True)
    name_of_field=models.CharField(verbose_name='Field Name', blank=True, max_length=100, null=True)
    group_1=models.CharField(verbose_name='Group 1', blank=True, max_length=100, null=True)
    group_2=models.CharField(verbose_name='Group 2', blank=True, max_length=100, null=True)
    group_3=models.CharField(verbose_name='Group 3', blank=True, max_length=100, null=True)
    type_of_field=models.CharField(verbose_name='Field Type', blank=True, max_length=100, null=True)#existing/Modified/Additional
    data_type=models.CharField(verbose_name='Data Type', blank=True, max_length=100, null=True)
    sbu=models.CharField(verbose_name='SBU', blank=True, max_length=100, null=True)#SBU_Applicability
    customer_type=models.CharField(verbose_name='Customer Type', blank=True, max_length=100, null=True)#SP/SH/BP/PY 
    applicability=models.CharField(verbose_name='Applicability', blank=True, max_length=100, null=True)
    possible_sources=models.CharField(verbose_name='Possible Sources', blank=True, max_length=100, null=True)
    remarks=models.CharField(verbose_name='Remarks', blank=True, max_length=100, null=True)
    purpose=models.CharField(verbose_name='Purpose', blank=True, max_length=100, null=True)
    legacy_field=models.CharField(verbose_name='Legacy Field', blank=True, max_length=100, null=True)
    comments= models.CharField(verbose_name='Comments', blank=True, max_length=100, null=True)
    mdg_rules_1=models.CharField(verbose_name='MDG Rule 1', blank=True, max_length=1000, null=True)
    mdg_rules_2=models.CharField(verbose_name='MDG Rule 2', blank=True, max_length=1000, null=True)
    mdg_rules_3=models.CharField(verbose_name='MDG Rule 3', blank=True, max_length=1000, null=True)
    mdg_rules_4=models.CharField(verbose_name='MDG Rule 4', blank=True, max_length=1000, null=True)
    mdg_rules_5=models.CharField(verbose_name='MDG Rule 5', blank=True, max_length=1000, null=True)
    action=models.CharField(verbose_name='Action', blank=True, max_length=100, null=True)
    created_by=models.CharField(verbose_name='Created By', blank=True, max_length=100, null=True)
    created_on=models.DateField(verbose_name='Created On', null=True, blank=True)
    updated_by=models.CharField(verbose_name='Updated By', blank=True, max_length=100, null=True)
    updated_on=models.DateField(verbose_name='Updated On', null=True, blank=True)

  
    class Meta:
        verbose_name="KDS"
        verbose_name_plural = "KDS`s"

        

class FIORI(models.Model):
    ...


class PERIPHERALS(models.Model):
    test = models.CharField(blank=True, max_length=100)


class CUTOVER(models.Model):
    test = models.CharField(blank=True, max_length=100)

class UTMASTER(models.Model):
    test_case_id = models.CharField(verbose_name='Test Case ID', max_length=100, unique=True)
    test_case_name = models.CharField(verbose_name='Test Case Name', max_length=100, unique=True)
    description = models.CharField(verbose_name='Description', max_length=500)
    business_process = models.CharField(verbose_name='Business Process', max_length=500)
    pre_requisites =models.CharField(verbose_name='Prerequisites', max_length=500)
    business_process_owner = models.CharField(verbose_name='Business Process Owner', max_length=500)
    test_owner_acc = models.CharField(verbose_name='Test Owner Acc.', max_length=300)
    test_cycle = models.CharField(verbose_name='Test Cycle', max_length=300)
    sap_sys_client = models.CharField(verbose_name='SAP System & Client', max_length=500)
    execution_date = models.DateField(verbose_name='Execution Date',null=True)
    process_desc = models.CharField(verbose_name='Process Description', max_length=300)

    def __str__(self) -> str:
        return self.test_case_name
    


class UNITTEST(models.Model):
    test_case = models.ForeignKey(UTMASTER, to_field='test_case_name',on_delete=models.SET_NULL, 
                            related_name='test_case_name_set', null=True)

    output_description = models.TextField(verbose_name='Output', null=True)
    attachment = models.FileField(verbose_name='Output Attachments', upload_to='uploads/', blank=True)
    
    error_description = models.TextField(verbose_name='Error Description', null=True)
    error_attachment = models.FileField(verbose_name='Error Attachments', upload_to='uploads/errors/', blank=True)

    remarks = models.TextField(verbose_name='Remarks', null=True)
    mark_for_deletion = models.BooleanField(verbose_name='Mark For Deletion', default=False)
    completed = models.BooleanField(verbose_name='Test Completed', default=False)
    created_by=models.CharField(verbose_name='Created By', blank=True, max_length=100, null=True)
    created_on=models.DateField(verbose_name='Created On', null=True, blank=True)
    updated_by=models.CharField(verbose_name='Updated By', blank=True, max_length=100, null=True)
    updated_on=models.DateField(verbose_name='Updated On', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Unit Test'        
        verbose_name_plural = 'Unit Tests'