from company.models import Company
from django.db import models


class YearSeasonManager(models.Manager):
    def create_ci(self, year, season):
        ci = self.create(year=year, season=season)
        return ci


class YearSeasonTableInfo(models.Model):

    year = models.CharField(max_length=10, help_text="年度")
    season = models.CharField(max_length=10, help_text="季度")

    objects = YearSeasonManager()

    def __str__(self):
        return f"年及季節代號: {self.id}"

    class Meta:
        db_table = "year_season"


class ComprehensiveIncomeManager(models.Manager):
    def create_ci(
        self,
        net_income_loss_of_interest,
        net_non_interest_income_loss,
        total_bad_debts_expense_and_guarantee_liability_provision,
        total_operating_expense,
        profit_loss_from_continuing_operations_before_tax,
        tax_income_expense,
        income_loss_from_continuing_operations_net_of_tax,
        total_income_loss_from_discontinued_operations,
        profit_loss_non_control_interest_before_combine_common_control,
        profit_loss,
        other_comprehensive_income_net_of_tax,
        total_comprehensive_income_net_of_tax,
        profit_loss_attributable_to_owners_of_parent,
        profit_loss_former_owner_business_combine_under_common_control,
        profit_loss_attributable_to_non_controlling_interests,
        comprehensive_income_attributable_to_owners_of_parent,
        comprehensive_income_former_combine_under_common_control,
        comprehensive_income_attributable_to_non_control_interests,
        total_primary_earnings_per_share,
        total_revenue,
        total_expenditure_and_expense,
        net_operating_income_loss,
        total_non_operating_income_and_expenses,
        income_tax_benefit_expense,
        profit_loss_from_continuing_operations,
        other_comprehensive_income,
        comprehensive_income_non_interest_before_combine_commoncontrol,
        total_comprehensive_income,
        total_operating_revenue,
        total_operating_costs,
        gross_profit_loss_from_operations,
        unrealized_profit_loss_from_sales,
        realized_profit_loss_on_from_sales,
        gross_profit_loss_from_operations_net,
        net_other_income_expenses,
        total_tax_expense_income,
        other_comprehensive_income_net,
        net_income_loss_except_interest,
        net_income_loss,
        total_bad_debt_expenses_and_guarantee_liability_provisions,
        total_net_change_in_provisions_for_insurance_liabilities,
        income_loss_from_continuing_operations,
        profit_loss_from_continuing_operations_before_income_tax,
        total_other_comprehensive_income,
        total_expenses,
        gains_loss_recognition_of_biological_asset_agriculture_produce,
        gain_loss_arise_change_fair_value_costs_biological_asset,
        company_id,
        year_season_id,
    ):
        ci = self.create(
            net_income_loss_of_interest=net_income_loss_of_interest,
            net_non_interest_income_loss=net_non_interest_income_loss,
            total_bad_debts_expense_and_guarantee_liability_provision=total_bad_debts_expense_and_guarantee_liability_provision,
            total_operating_expense=total_operating_expense,
            profit_loss_from_continuing_operations_before_tax=profit_loss_from_continuing_operations_before_tax,
            tax_income_expense=tax_income_expense,
            income_loss_from_continuing_operations_net_of_tax=income_loss_from_continuing_operations_net_of_tax,
            total_income_loss_from_discontinued_operations=total_income_loss_from_discontinued_operations,
            profit_loss_non_control_interest_before_combine_common_control=profit_loss_non_control_interest_before_combine_common_control,
            profit_loss=profit_loss,
            other_comprehensive_income_net_of_tax=other_comprehensive_income_net_of_tax,
            total_comprehensive_income_net_of_tax=total_comprehensive_income_net_of_tax,
            profit_loss_attributable_to_owners_of_parent=profit_loss_attributable_to_owners_of_parent,
            profit_loss_former_owner_business_combine_under_common_control=profit_loss_former_owner_business_combine_under_common_control,
            profit_loss_attributable_to_non_controlling_interests=profit_loss_attributable_to_non_controlling_interests,
            comprehensive_income_attributable_to_owners_of_parent=comprehensive_income_attributable_to_owners_of_parent,
            comprehensive_income_former_combine_under_common_control=comprehensive_income_former_combine_under_common_control,
            comprehensive_income_attributable_to_non_control_interests=comprehensive_income_attributable_to_non_control_interests,
            total_primary_earnings_per_share=total_primary_earnings_per_share,
            total_revenue=total_revenue,
            total_expenditure_and_expense=total_expenditure_and_expense,
            net_operating_income_loss=net_operating_income_loss,
            total_non_operating_income_and_expenses=total_non_operating_income_and_expenses,
            income_tax_benefit_expense=income_tax_benefit_expense,
            profit_loss_from_continuing_operations=profit_loss_from_continuing_operations,
            other_comprehensive_income=other_comprehensive_income,
            comprehensive_income_non_interest_before_combine_commoncontrol=comprehensive_income_non_interest_before_combine_commoncontrol,
            total_comprehensive_income=total_comprehensive_income,
            total_operating_revenue=total_operating_revenue,
            total_operating_costs=total_operating_costs,
            gross_profit_loss_from_operations=gross_profit_loss_from_operations,
            unrealized_profit_loss_from_sales=unrealized_profit_loss_from_sales,
            realized_profit_loss_on_from_sales=realized_profit_loss_on_from_sales,
            gross_profit_loss_from_operations_net=gross_profit_loss_from_operations_net,
            net_other_income_expenses=net_other_income_expenses,
            total_tax_expense_income=total_tax_expense_income,
            other_comprehensive_income_net=other_comprehensive_income_net,
            net_income_loss_except_interest=net_income_loss_except_interest,
            net_income_loss=net_income_loss,
            total_bad_debt_expenses_and_guarantee_liability_provisions=total_bad_debt_expenses_and_guarantee_liability_provisions,
            total_net_change_in_provisions_for_insurance_liabilities=total_net_change_in_provisions_for_insurance_liabilities,
            income_loss_from_continuing_operations=income_loss_from_continuing_operations,
            profit_loss_from_continuing_operations_before_income_tax=profit_loss_from_continuing_operations_before_income_tax,
            total_other_comprehensive_income=total_other_comprehensive_income,
            total_expenses=total_expenses,
            gains_loss_recognition_of_biological_asset_agriculture_produce=gains_loss_recognition_of_biological_asset_agriculture_produce,
            gain_loss_arise_change_fair_value_costs_biological_asset=gain_loss_arise_change_fair_value_costs_biological_asset,
            company_id=company_id,
            year_season_id=year_season_id,
        )
        return ci

    # def get_latest_date(self):
    #     latest_data = self.latest("year_season_id").trade_date
    #     return latest_data


class ComprehensiveIncome(models.Model):

    year_season = models.ForeignKey(
        YearSeasonTableInfo, on_delete=models.CASCADE, help_text="年及季節代號"
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, help_text="公司表代號")
    net_income_loss_of_interest = models.FloatField(null=True, help_text="利息淨收益")
    net_non_interest_income_loss = models.FloatField(null=True, help_text="利息以外淨損益")
    total_bad_debts_expense_and_guarantee_liability_provision = models.FloatField(
        null=True, help_text="呆帳費用及保證責任準備提存（各項提存）"
    )
    total_operating_expense = models.FloatField(null=True, help_text="營業費用")
    profit_loss_from_continuing_operations_before_tax = models.FloatField(
        null=True, help_text="繼續營業單位稅前淨利（淨損）"
    )
    tax_income_expense = models.FloatField(null=True, help_text="所得稅（費用）利益")
    income_loss_from_continuing_operations_net_of_tax = models.FloatField(
        null=True, help_text="繼續營業單位本期稅後淨利（淨損）"
    )
    total_income_loss_from_discontinued_operations = models.FloatField(
        null=True, help_text="停業單位損益"
    )
    profit_loss_non_control_interest_before_combine_common_control = models.FloatField(
        null=True, help_text="合併前非屬共同控制股權損益"
    )
    profit_loss = models.FloatField(null=True, help_text="本期稅後淨利（淨損）")
    other_comprehensive_income_net_of_tax = models.FloatField(
        null=True, help_text="其他綜合損益（稅後）"
    )
    total_comprehensive_income_net_of_tax = models.FloatField(
        null=True, help_text="本期綜合損益總額（稅後）"
    )
    profit_loss_attributable_to_owners_of_parent = models.FloatField(
        null=True, help_text="淨利（損）歸屬於母公司業主"
    )
    profit_loss_former_owner_business_combine_under_common_control = models.FloatField(
        null=True, help_text="淨利（損）歸屬於共同控制下前手權益"
    )
    profit_loss_attributable_to_non_controlling_interests = models.FloatField(
        null=True, help_text="淨利（損）歸屬於非控制權益"
    )
    comprehensive_income_attributable_to_owners_of_parent = models.FloatField(
        null=True, help_text="綜合損益總額歸屬於母公司業主"
    )
    comprehensive_income_former_combine_under_common_control = models.FloatField(
        null=True, help_text="綜合損益總額歸屬於共同控制下前手權益"
    )
    comprehensive_income_attributable_to_non_control_interests = models.FloatField(
        null=True, help_text="綜合損益總額歸屬於非控制權益"
    )
    total_primary_earnings_per_share = models.FloatField(
        null=True, help_text="基本每股盈餘（元）"
    )
    total_revenue = models.FloatField(null=True, help_text="收益")
    total_expenditure_and_expense = models.FloatField(null=True, help_text="支出及費用")
    net_operating_income_loss = models.FloatField(null=True, help_text="營業利益")
    total_non_operating_income_and_expenses = models.FloatField(
        null=True, help_text="營業外損益"
    )
    income_tax_benefit_expense = models.FloatField(null=True, help_text="所得稅利益（費用）")
    profit_loss_from_continuing_operations = models.FloatField(
        null=True, help_text="繼續營業單位本期淨利（淨損）"
    )
    other_comprehensive_income = models.FloatField(
        null=True, help_text="本期其他綜合損益（稅後淨額）"
    )
    comprehensive_income_non_interest_before_combine_commoncontrol = models.FloatField(
        null=True, help_text="合併前非屬共同控制股權綜合損益淨額"
    )
    total_comprehensive_income = models.FloatField(null=True, help_text="本期綜合損益總額")
    total_operating_revenue = models.FloatField(null=True, help_text="營業收入")
    total_operating_costs = models.FloatField(null=True, help_text="營業成本")
    gross_profit_loss_from_operations = models.FloatField(
        null=True, help_text="營業毛利（毛損）"
    )
    unrealized_profit_loss_from_sales = models.FloatField(
        null=True, help_text="未實現銷貨（損）益"
    )
    realized_profit_loss_on_from_sales = models.FloatField(
        null=True, help_text="已實現銷貨（損）益"
    )
    gross_profit_loss_from_operations_net = models.FloatField(
        null=True, help_text="營業毛利（毛損）淨額"
    )
    net_other_income_expenses = models.FloatField(null=True, help_text="其他收益及費損淨額")
    total_tax_expense_income = models.FloatField(null=True, help_text="所得稅費用（利益）")
    other_comprehensive_income_net = models.FloatField(
        null=True, help_text="其他綜合損益（淨額）"
    )
    net_income_loss_except_interest = models.FloatField(null=True, help_text="利息以外淨收益")
    net_income_loss = models.FloatField(null=True, help_text="淨收益")
    total_bad_debt_expenses_and_guarantee_liability_provisions = models.FloatField(
        null=True, help_text="呆帳費用及保證責任準備提存"
    )
    total_net_change_in_provisions_for_insurance_liabilities = models.FloatField(
        null=True, help_text="保險負債準備淨變動"
    )
    income_loss_from_continuing_operations = models.FloatField(
        null=True, help_text="繼續營業單位稅前損益"
    )
    profit_loss_from_continuing_operations_before_income_tax = models.FloatField(
        null=True, help_text="繼續營業單位稅前純益（純損）"
    )
    total_other_comprehensive_income = models.FloatField(
        null=True, help_text="其他綜合損益（稅後淨額）"
    )
    total_expenses = models.FloatField(null=True, help_text="支出")
    gains_loss_recognition_of_biological_asset_agriculture_produce = models.FloatField(
        null=True, help_text="原始認列生物資產及農產品之利益（損失）"
    )
    gain_loss_arise_change_fair_value_costs_biological_asset = models.FloatField(
        null=True, help_text="生物資產當期公允價值減出售成本之變動利益（損失）"
    )

    objects = ComprehensiveIncomeManager()

    def __str__(self):
        return f"綜合彙整報表： {self.id}"

    class Meta:
        db_table = "comprehensive_income"


class BalanceSheetManager(models.Manager):
    def create_ci(
        self,
        total_cash_and_cash_equivalent,
        total_due_from_central_bank_and_call_loan_to_bank,
        total_financial_assets_at_fair_value_through_profit_or_loss,
        derivative_financial_asset_for_hedging_net,
        securitie_purchased_under_resell_agreement_net,
        total_current_tax_asset,
        discounts_and_loans_net,
        available_for_sale_financial_assets_net,
        held_to_maturity_financial_assets_net,
        investments_measured_by_equity_method_net,
        restricted_assets_net,
        other_financial_assets_net,
        property_and_equipment_net,
        investment_property_invest_net,
        intangible_assets_net,
        total_deferred_tax_assets,
        other_assets_net,
        total_assets,
        total_deposits_from_the_central_bank_and_banks,
        total_due_to_the_central_bank_and_banks,
        total_financial_liabilities_at_fair_value_profit_or_loss,
        hedge_derivative_financial_liability_net,
        total_notes_and_bonds_issued_under_repurchase_agreement,
        total_payables,
        total_current_tax_liabilities,
        total_liabilities_related_assets_classified_held_for_sale,
        total_deposits_and_remittances,
        total_bank_notes_payable,
        total_bonds_payable,
        total_preferred_stock_liabilities,
        total_other_financial_liabilities,
        total_provisions,
        total_deferred_income_tax_liabilities,
        total_other_liabilities,
        total_liabilities,
        total_capital,
        total_capital_surplus,
        total_retained_earnings,
        total_other_equity_interest,
        total_treasury_shares,
        total_equity_attributable_to_owners_of_parent,
        equity_to_former_owner_business_combination_common_control,
        equity_non_control_interest_business_combine_common_control,
        total_non_controlling_interests,
        total_equity,
        number_of_share_capital_awaiting_retirement,
        number_treasury_share_acquired_by_company_and_subsidiaries,
        equivalent_issued_shares_of_advance_receipts_for_common_stock,
        book_value_per_share,
        total_current_assets,
        non_current_assets_net,
        total_current_liabilities,
        total_non_current_liabilities,
        equity,
        number_of_shares_entity_held_entity_and_its_subsidiaries,
        due_from_the_central_bank_and_call_loans_to_banks,
        derivative_financial_assets_for_hedging,
        securities_purchased_under_resell_agreements,
        reinsurance_contract_assets_net,
        investment_property_net,
        deposits_from_the_central_bank_and_banks,
        derivative_financial_liabilities_for_hedging,
        commercial_papers_issued_net,
        bonds_payable,
        total_other_borrowings,
        receivables_net,
        assets_classified_as_held_for_sale_net,
        non_current_asset_disposal_group_held_distribution_owners,
        total_investments,
        total_reinsurance_assets,
        total_property_and_equipment,
        total_intangible_assets,
        total_other_assets,
        assets_on_insurance_product_separated_account,
        short_term_liabilities_net,
        financial_liabilities_at_cost,
        total_insurance_liabilities,
        reserve_for_insurance_with_nature_of_financial_instrument,
        reserve_for_foreign_exchange_valuation,
        liabilities_on_insurance_product_separated_account,
        treasury_shares,
        assets_classified_as_held_for_distribution_to_owners_net,
        financial_assets_fair_value_other_comprehensive_income,
        investments_in_debt_instruments_at_amortised_cost,
        current_tax_assets,
        right_of_use_assets_net,
        lease_liabilities,
        right_of_use_assets,
        total_equity_security_token_Offer,
        equity_security_token_Offer,
        company_id,
        year_season_id,
    ):
        ci = self.create(
            total_cash_and_cash_equivalent=total_cash_and_cash_equivalent,
            total_due_from_central_bank_and_call_loan_to_bank=total_due_from_central_bank_and_call_loan_to_bank,
            total_financial_assets_at_fair_value_through_profit_or_loss=total_financial_assets_at_fair_value_through_profit_or_loss,
            derivative_financial_asset_for_hedging_net=derivative_financial_asset_for_hedging_net,
            securitie_purchased_under_resell_agreement_net=securitie_purchased_under_resell_agreement_net,
            total_current_tax_asset=total_current_tax_asset,
            discounts_and_loans_net=discounts_and_loans_net,
            available_for_sale_financial_assets_net=available_for_sale_financial_assets_net,
            held_to_maturity_financial_assets_net=held_to_maturity_financial_assets_net,
            investments_measured_by_equity_method_net=investments_measured_by_equity_method_net,
            restricted_assets_net=restricted_assets_net,
            other_financial_assets_net=other_financial_assets_net,
            property_and_equipment_net=property_and_equipment_net,
            investment_property_invest_net=investment_property_invest_net,
            intangible_assets_net=intangible_assets_net,
            total_deferred_tax_assets=total_deferred_tax_assets,
            other_assets_net=other_assets_net,
            total_assets=total_assets,
            total_deposits_from_the_central_bank_and_banks=total_deposits_from_the_central_bank_and_banks,
            total_due_to_the_central_bank_and_banks=total_due_to_the_central_bank_and_banks,
            total_financial_liabilities_at_fair_value_profit_or_loss=total_financial_liabilities_at_fair_value_profit_or_loss,
            hedge_derivative_financial_liability_net=hedge_derivative_financial_liability_net,
            total_notes_and_bonds_issued_under_repurchase_agreement=total_notes_and_bonds_issued_under_repurchase_agreement,
            total_payables=total_payables,
            total_current_tax_liabilities=total_current_tax_liabilities,
            total_liabilities_related_assets_classified_held_for_sale=total_liabilities_related_assets_classified_held_for_sale,
            total_deposits_and_remittances=total_deposits_and_remittances,
            total_bank_notes_payable=total_bank_notes_payable,
            total_bonds_payable=total_bonds_payable,
            total_preferred_stock_liabilities=total_preferred_stock_liabilities,
            total_other_financial_liabilities=total_other_financial_liabilities,
            total_provisions=total_provisions,
            total_deferred_income_tax_liabilities=total_deferred_income_tax_liabilities,
            total_other_liabilities=total_other_liabilities,
            total_liabilities=total_liabilities,
            total_capital=total_capital,
            total_capital_surplus=total_capital_surplus,
            total_retained_earnings=total_retained_earnings,
            total_other_equity_interest=total_other_equity_interest,
            total_treasury_shares=total_treasury_shares,
            total_equity_attributable_to_owners_of_parent=total_equity_attributable_to_owners_of_parent,
            equity_to_former_owner_business_combination_common_control=equity_to_former_owner_business_combination_common_control,
            equity_non_control_interest_business_combine_common_control=equity_non_control_interest_business_combine_common_control,
            total_non_controlling_interests=total_non_controlling_interests,
            total_equity=total_equity,
            number_of_share_capital_awaiting_retirement=number_of_share_capital_awaiting_retirement,
            number_treasury_share_acquired_by_company_and_subsidiaries=number_treasury_share_acquired_by_company_and_subsidiaries,
            equivalent_issued_shares_of_advance_receipts_for_common_stock=equivalent_issued_shares_of_advance_receipts_for_common_stock,
            book_value_per_share=book_value_per_share,
            total_current_assets=total_current_assets,
            non_current_assets_net=non_current_assets_net,
            total_current_liabilities=total_current_liabilities,
            total_non_current_liabilities=total_non_current_liabilities,
            equity=equity,
            number_of_shares_entity_held_entity_and_its_subsidiaries=number_of_shares_entity_held_entity_and_its_subsidiaries,
            due_from_the_central_bank_and_call_loans_to_banks=due_from_the_central_bank_and_call_loans_to_banks,
            derivative_financial_assets_for_hedging=derivative_financial_assets_for_hedging,
            securities_purchased_under_resell_agreements=securities_purchased_under_resell_agreements,
            reinsurance_contract_assets_net=reinsurance_contract_assets_net,
            investment_property_net=investment_property_net,
            deposits_from_the_central_bank_and_banks=deposits_from_the_central_bank_and_banks,
            derivative_financial_liabilities_for_hedging=derivative_financial_liabilities_for_hedging,
            commercial_papers_issued_net=commercial_papers_issued_net,
            bonds_payable=bonds_payable,
            total_other_borrowings=total_other_borrowings,
            receivables_net=receivables_net,
            assets_classified_as_held_for_sale_net=assets_classified_as_held_for_sale_net,
            non_current_asset_disposal_group_held_distribution_owners=non_current_asset_disposal_group_held_distribution_owners,
            total_investments=total_investments,
            total_reinsurance_assets=total_reinsurance_assets,
            total_property_and_equipment=total_property_and_equipment,
            total_intangible_assets=total_intangible_assets,
            total_other_assets=total_other_assets,
            assets_on_insurance_product_separated_account=assets_on_insurance_product_separated_account,
            short_term_liabilities_net=short_term_liabilities_net,
            financial_liabilities_at_cost=financial_liabilities_at_cost,
            total_insurance_liabilities=total_insurance_liabilities,
            reserve_for_insurance_with_nature_of_financial_instrument=reserve_for_insurance_with_nature_of_financial_instrument,
            reserve_for_foreign_exchange_valuation=reserve_for_foreign_exchange_valuation,
            liabilities_on_insurance_product_separated_account=liabilities_on_insurance_product_separated_account,
            treasury_shares=treasury_shares,
            assets_classified_as_held_for_distribution_to_owners_net=assets_classified_as_held_for_distribution_to_owners_net,
            financial_assets_fair_value_other_comprehensive_income=financial_assets_fair_value_other_comprehensive_income,
            investments_in_debt_instruments_at_amortised_cost=investments_in_debt_instruments_at_amortised_cost,
            current_tax_assets=current_tax_assets,
            right_of_use_assets_net=right_of_use_assets_net,
            lease_liabilities=lease_liabilities,
            right_of_use_assets=right_of_use_assets,
            total_equity_security_token_Offer=total_equity_security_token_Offer,
            equity_security_token_Offer=equity_security_token_Offer,
            company_id=company_id,
            year_season_id=year_season_id,
        )
        return ci


class BalanceSheet(models.Model):

    year_season = models.ForeignKey(
        YearSeasonTableInfo, on_delete=models.CASCADE, help_text="年及季節代號"
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, help_text="公司表代號")
    total_cash_and_cash_equivalent = models.FloatField(null=True, help_text="現金及約當現金")
    total_due_from_central_bank_and_call_loan_to_bank = models.FloatField(
        null=True, help_text="存放央行及拆借銀行同業"
    )
    total_financial_assets_at_fair_value_through_profit_or_loss = models.FloatField(
        null=True, help_text="透過損益按公允價值衡量之金融資產"
    )
    derivative_financial_asset_for_hedging_net = models.FloatField(
        null=True, help_text="避險之衍生金融資產淨額"
    )
    securitie_purchased_under_resell_agreement_net = models.FloatField(
        null=True, help_text="附賣回票券及債券投資淨額"
    )
    total_current_tax_asset = models.FloatField(null=True, help_text="當期所得稅資產")
    discounts_and_loans_net = models.FloatField(null=True, help_text="貼現及放款－淨額")
    available_for_sale_financial_assets_net = models.FloatField(
        null=True, help_text="備供出售金融資產－淨額"
    )
    held_to_maturity_financial_assets_net = models.FloatField(
        null=True, help_text="持有至到期日金融資產－淨額"
    )
    investments_measured_by_equity_method_net = models.FloatField(
        null=True, help_text="採用權益法之投資－淨額"
    )
    restricted_assets_net = models.FloatField(null=True, help_text="受限制資產－淨額")
    other_financial_assets_net = models.FloatField(null=True, help_text="其他金融資產－淨額")
    property_and_equipment_net = models.FloatField(null=True, help_text="不動產及設備－淨額")
    investment_property_invest_net = models.FloatField(
        null=True, help_text="投資性不動產投資－淨額"
    )
    intangible_assets_net = models.FloatField(null=True, help_text="無形資產－淨額")
    total_deferred_tax_assets = models.FloatField(null=True, help_text="遞延所得稅資產")
    other_assets_net = models.FloatField(null=True, help_text="其他資產－淨額")
    total_assets = models.FloatField(null=True, help_text="資產總額")
    total_deposits_from_the_central_bank_and_banks = models.FloatField(
        null=True, help_text="央行及銀行同業存款"
    )
    total_due_to_the_central_bank_and_banks = models.FloatField(
        null=True, help_text="央行及同業融資"
    )
    total_financial_liabilities_at_fair_value_profit_or_loss = models.FloatField(
        null=True, help_text="透過損益按公允價值衡量之金融負債"
    )
    hedge_derivative_financial_liability_net = models.FloatField(
        null=True, help_text="避險之衍生金融負債－淨額"
    )
    total_notes_and_bonds_issued_under_repurchase_agreement = models.FloatField(
        null=True, help_text="附買回票券及債券負債"
    )
    total_payables = models.FloatField(null=True, help_text="應付款項")
    total_current_tax_liabilities = models.FloatField(null=True, help_text="當期所得稅負債")
    total_liabilities_related_assets_classified_held_for_sale = models.FloatField(
        null=True, help_text="與待出售資產直接相關之負債"
    )
    total_deposits_and_remittances = models.FloatField(null=True, help_text="存款及匯款")
    total_bank_notes_payable = models.FloatField(null=True, help_text="應付金融債券")
    total_bonds_payable = models.FloatField(null=True, help_text="應付公司債")
    total_preferred_stock_liabilities = models.FloatField(null=True, help_text="特別股負債")
    total_other_financial_liabilities = models.FloatField(null=True, help_text="其他金融負債")
    total_provisions = models.FloatField(null=True, help_text="負債準備")
    total_deferred_income_tax_liabilities = models.FloatField(
        null=True, help_text="遞延所得稅負債"
    )
    total_other_liabilities = models.FloatField(null=True, help_text="其他負債")
    total_liabilities = models.FloatField(null=True, help_text="負債總額")
    total_capital = models.FloatField(null=True, help_text="股本")
    total_capital_surplus = models.FloatField(null=True, help_text="資本公積")
    total_retained_earnings = models.FloatField(null=True, help_text="保留盈餘")
    total_other_equity_interest = models.FloatField(null=True, help_text="其他權益")
    total_treasury_shares = models.FloatField(null=True, help_text="庫藏股票")
    total_equity_attributable_to_owners_of_parent = models.FloatField(
        null=True, help_text="歸屬於母公司業主之權益合計"
    )
    equity_to_former_owner_business_combination_common_control = models.FloatField(
        null=True, help_text="共同控制下前手權益"
    )
    equity_non_control_interest_business_combine_common_control = models.FloatField(
        null=True, help_text="合併前非屬共同控制股權"
    )
    total_non_controlling_interests = models.FloatField(null=True, help_text="非控制權益")
    total_equity = models.FloatField(null=True, help_text="權益總額")
    number_of_share_capital_awaiting_retirement = models.FloatField(
        null=True, help_text="待註銷股本股數（單位：股）"
    )
    number_treasury_share_acquired_by_company_and_subsidiaries = models.FloatField(
        null=True, help_text="母公司暨子公司所持有之母公司庫藏股股數（單位：股）"
    )
    equivalent_issued_shares_of_advance_receipts_for_common_stock = models.FloatField(
        null=True, help_text="預收股款（權益項下）之約當發行股數（單位：股）"
    )
    book_value_per_share = models.FloatField(null=True, help_text="每股參考淨值")
    total_current_assets = models.FloatField(null=True, help_text="流動資產")
    non_current_assets_net = models.FloatField(null=True, help_text="非流動資產")
    total_current_liabilities = models.FloatField(null=True, help_text="流動負債")
    total_non_current_liabilities = models.FloatField(null=True, help_text="非流動負債")
    equity = models.FloatField(null=True, help_text="權益合計")
    number_of_shares_entity_held_entity_and_its_subsidiaries = models.FloatField(
        null=True, help_text="母公司暨子公司持有之母公司庫藏股股數（單位：股）"
    )
    due_from_the_central_bank_and_call_loans_to_banks = models.FloatField(
        null=True, help_text="存放央行及拆借金融同業"
    )
    derivative_financial_assets_for_hedging = models.FloatField(
        null=True, help_text="避險之衍生金融資產"
    )
    securities_purchased_under_resell_agreements = models.FloatField(
        null=True, help_text="附賣回票券及債券投資"
    )
    reinsurance_contract_assets_net = models.FloatField(
        null=True, help_text="再保險合約資產－淨額"
    )
    investment_property_net = models.FloatField(null=True, help_text="投資性不動產－淨額")
    deposits_from_the_central_bank_and_banks = models.FloatField(
        null=True, help_text="央行及金融同業存款"
    )
    derivative_financial_liabilities_for_hedging = models.FloatField(
        null=True, help_text="避險之衍生金融負債"
    )
    commercial_papers_issued_net = models.FloatField(null=True, help_text="應付商業本票－淨額")
    bonds_payable = models.FloatField(null=True, help_text="應付債券")
    total_other_borrowings = models.FloatField(null=True, help_text="其他借款")
    receivables_net = models.FloatField(null=True, help_text="應收款項")
    assets_classified_as_held_for_sale_net = models.FloatField(
        null=True, help_text="待出售資產"
    )
    non_current_asset_disposal_group_held_distribution_owners = models.FloatField(
        null=True, help_text="待分配予業主之資產（或處分群組）"
    )
    total_investments = models.FloatField(null=True, help_text="投資")
    total_reinsurance_assets = models.FloatField(null=True, help_text="再保險合約資產")
    total_property_and_equipment = models.FloatField(null=True, help_text="不動產及設備")
    total_intangible_assets = models.FloatField(null=True, help_text="無形資產")
    total_other_assets = models.FloatField(null=True, help_text="其他資產")
    assets_on_insurance_product_separated_account = models.FloatField(
        null=True, help_text="分離帳戶保險商品資產"
    )
    short_term_liabilities_net = models.FloatField(null=True, help_text="短期債務")
    financial_liabilities_at_cost = models.FloatField(null=True, help_text="以成本衡量之金融負債")
    total_insurance_liabilities = models.FloatField(null=True, help_text="保險負債")
    reserve_for_insurance_with_nature_of_financial_instrument = models.FloatField(
        null=True, help_text="具金融商品性質之保險契約準備"
    )
    reserve_for_foreign_exchange_valuation = models.FloatField(
        null=True, help_text="外匯價格變動準備"
    )
    liabilities_on_insurance_product_separated_account = models.FloatField(
        null=True, help_text="分離帳戶保險商品負債"
    )
    treasury_shares = models.FloatField(null=True, help_text="庫藏股")
    assets_classified_as_held_for_distribution_to_owners_net = models.FloatField(
        null=True, help_text="待分配予業主之資產－淨額"
    )
    financial_assets_fair_value_other_comprehensive_income = models.FloatField(
        null=True, help_text="透過其他綜合損益按公允價值衡量之金融資產"
    )
    investments_in_debt_instruments_at_amortised_cost = models.FloatField(
        null=True, help_text="按攤銷後成本衡量之債務工具投資"
    )
    current_tax_assets = models.FloatField(null=True, help_text="本期所得稅資產")
    right_of_use_assets_net = models.FloatField(null=True, help_text="使用權資產－淨額")
    lease_liabilities = models.FloatField(null=True, help_text="租賃負債")
    right_of_use_assets = models.FloatField(null=True, help_text="使用權資產")
    total_equity_security_token_Offer = models.FloatField(
        null=True, help_text="權益─具證券性質之虛擬通貨"
    )
    equity_security_token_Offer = models.FloatField(
        null=True, help_text="權益－具證券性質之虛擬通貨"
    )

    objects = BalanceSheetManager()

    def __str__(self):
        return f"負債資產: {self.id}"

    class Meta:
        db_table = "balance_sheet"
