from django.db import models


class CompanyTypeManager(models.Manager):
    def create_ci(self, company_type):
        ci = self.create(company_type=company_type)
        return ci


class CompanyType(models.Model):

    company_type = models.CharField(max_length=50, help_text="產業類別")

    objects = CompanyTypeManager()

    def __str__(self):
        return f"公司種類: {self.company_type}"

    class Meta:
        db_table = "company_type"


class CompanyManager(models.Manager):
    def create_ci(self, company_code, company_name, company_abbreviation, company_type):
        ci = self.create(
            company_code=company_code,
            company_name=company_name,
            company_abbreviation=company_abbreviation,
            company_type=company_type,
        )
        return ci


class Company(models.Model):

    company_code = models.CharField(max_length=50, help_text="公司代號")
    company_name = models.CharField(max_length=50, help_text="公司名稱")
    company_abbreviation = models.CharField(max_length=50, help_text="公司簡稱")
    company_type = models.ForeignKey(
        CompanyType,
        related_name="company",
        on_delete=models.CASCADE,
        help_text="公司種類ID",
    )

    objects = CompanyManager()

    def __str__(self):
        return f"公司表編號: {self.id}"

    class Meta:
        db_table = "company"
