import json
import requests


def send(type):
    header = {
        'Cookie': '',
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': '127.0.0.1:4523',
        'Connection': 'keep-alive'
    }

    if type == '批发销售单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/WholesaleOrderByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "670FC63F-4B58-47D8-9B13-866D4A9318D9",
                    "WONumber": "76FE4BB",
                    "SerialNumberTime": "2022-08-25",
                    "SalesOrganizationNo": "",
                    "SalesOrganization": "",
                    "SalesOrganizationType": "",
                    "Seller": "",
                    "Status": ""
                }
            ]
        }
        )
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/WholesaleOrderDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "670FC63F-4B58-47D8-9B13-866D4A9318D9",
                    "WONumber": "76FE4BB",
                    "Psn": "14283",
                    "Quantity": 100,
                    "Price": 13.15,
                    "PriceTaxi": 14.728,
                    "PurchasePrice": 12,
                    "TaxRate": 12,
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "DrugsBase_DrugName": "尿素维E乳膏",
                    "DrugsBase_Specification": "40g",
                    "DrugsBase_Manufacturer": "上海中华药业南通有限公司",
                    "ApprovalNumber": "",
                    "BatchNumber": "",
                    "ProductionDate": "2021-2-12",
                    "Spxq": "2025-2-12",
                    "YouXq": "2025-2-12",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 14.728
                }
            ]
        }
        )
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail
    elif type == '零售销售单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/RetailSalesOrderByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2113",
                    "RSONumber": "E381DB1",
                    "SerialNumberTime": "2022-08-25",
                    "SalesOrganizationNo": "sc0001",
                    "SalesOrganization": "成都青羊店",
                    "SalesOrganizationType": "0",
                    "Customer": "soso",
                    "Seller": "ZW",
                    "Status": ""
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2121",
                    "RSONumber": "E381DB2",
                    "SerialNumberTime": "2022-11-25",
                    "SalesOrganizationNo": "sc0001",
                    "SalesOrganization": "成都青羊店",
                    "SalesOrganizationType": "0",
                    "Customer": "soso",
                    "Seller": "ZW",
                    "Status": ""
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2122",
                    "RSONumber": "E381DB3",
                    "SerialNumberTime": "2022-12-25",
                    "SalesOrganizationNo": "sc0001",
                    "SalesOrganization": "成都青羊店",
                    "SalesOrganizationType": "0",
                    "Customer": "soso",
                    "Seller": "ZW",
                    "Status": ""
                }
            ]
        }
        )
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/RetailSalesOrderDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2114",
                    "RSONumber": "E381DB1",
                    "Psn": "751568",
                    "Quantity": 100,
                    "Price": 10,
                    "PriceTaxi": 12,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-卖品赠本",
                    "DrugsBase_Specification": "5mg*12袋",
                    "DrugsBase_Manufacturer": "海南新世通制药有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2123",
                    "RSONumber": "E381DB2",
                    "Psn": "751568",
                    "Quantity": 100,
                    "Price": 10,
                    "PriceTaxi": 12,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-卖品赠本",
                    "DrugsBase_Specification": "5mg*12袋",
                    "DrugsBase_Manufacturer": "海南新世通制药有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2124",
                    "RSONumber": "E381DB3",
                    "Psn": "751568",
                    "Quantity": 100,
                    "Price": 10,
                    "PriceTaxi": 12,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-卖品赠本",
                    "DrugsBase_Specification": "5mg*12袋",
                    "DrugsBase_Manufacturer": "海南新世通制药有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2126",
                    "RSONumber": "E381DB3",
                    "Psn": "90227378",
                    "Quantity": 100,
                    "Price": 10,
                    "PriceTaxi": 12,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-卖品赠本",
                    "DrugsBase_Specification": "5mg*12袋",
                    "DrugsBase_Manufacturer": "海南新世通制药有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2115",
                    "RSONumber": "E381DB1",
                    "Psn": "90227378",
                    "Quantity": 200,
                    "Price": 15,
                    "PriceTaxi": 20,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-卖品2赠品非本品",
                    "DrugsBase_Specification": "60ml",
                    "DrugsBase_Manufacturer": "江西正信堂生物科技有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2116",
                    "RSONumber": "E381DB1",
                    "Psn": "210085",
                    "Quantity": 300,
                    "Price": 30,
                    "PriceTaxi": 40,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-卖品3赠非本品",
                    "DrugsBase_Specification": "60ml",
                    "DrugsBase_Manufacturer": "江西正信堂生物科技有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2117",
                    "RSONumber": "E381DB1",
                    "Psn": "751568",
                    "Quantity": 20,
                    "Price": 100,
                    "PriceTaxi": 0.01,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-赠品1",
                    "DrugsBase_Specification": "60ml",
                    "DrugsBase_Manufacturer": "江西正信堂生物科技有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2125",
                    "RSONumber": "E381DB2",
                    "Psn": "751568",
                    "Quantity": 20,
                    "Price": 100,
                    "PriceTaxi": 0.01,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-赠品1",
                    "DrugsBase_Specification": "60ml",
                    "DrugsBase_Manufacturer": "江西正信堂生物科技有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2118",
                    "RSONumber": "E381DB1",
                    "Psn": "90227378",
                    "Quantity": 0,
                    "Price": 10,
                    "PriceTaxi": 0.01,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-赠品2",
                    "DrugsBase_Specification": "60ml",
                    "DrugsBase_Manufacturer": "江西正信堂生物科技有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2119",
                    "RSONumber": "E381DB1",
                    "Psn": "210085",
                    "Quantity": 70,
                    "Price": 10,
                    "PriceTaxi": 0.01,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-赠品3",
                    "DrugsBase_Specification": "60ml",
                    "DrugsBase_Manufacturer": "江西正信堂生物科技有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                },
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2120",
                    "RSONumber": "E381DB1",
                    "Psn": "84570",
                    "Quantity": 100,
                    "Price": 10,
                    "PriceTaxi": 0.01,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏-赠品4",
                    "DrugsBase_Specification": "60ml",
                    "DrugsBase_Manufacturer": "江西正信堂生物科技有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 14
                }
            ]
        }
        )
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail
    elif type == '配送出库单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseDeliveryByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "822777EB-701A-4169-946C-B5F183EC503433",
                    "DeliNumber": "996DFC5",
                    "SerialNumberTime": "2022-08-25",
                    "SupplierNameId": "",
                    "SupplierName": "",
                    "SalesOrganizationNo": "sc0001",
                    "SalesOrganization": "成都青羊店",
                    "SalesOrganizationType": "0",
                    "TotalAmount": 778.4,
                    "TaxiAmount": 94.2674,
                    "TotalPriceTax": 122.5476,
                    "Status": ""
                }
            ]
        }
        )
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseDeliveryDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "822777EB-701A-4169-946C-B5F183EC503433",
                    "DeliNumber": "996DFC5",
                    "Psn": "90227378",
                    "QuantityReal": 100,
                    "Quantity": 100,
                    "BuyCount": 100,
                    "Price": 50,
                    "PriceTaxi": 53,
                    "DrugsBase_DrugName": "尿素维E乳膏",
                    "DrugsBase_Specification": "40g",
                    "DrugsBase_Manufacturer": "上海中华药业南通有限公司",
                    "ApprovalNumber": "",
                    "BatchNumber": "",
                    "ProductionDate": "",
                    "Stock_Unit": "",
                    "Valuation_Unit": "",
                    "Valuation_Number": "",
                    "Buy_Unit": "",
                    "Spxq": "",
                    "YouXq": "",
                    "BatchPurchasePrice_Detail": 53
                }
            ]
        })
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main.text, response_detail.text
    elif type == '采购入库单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurcWarehousingByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "2CDD5D28-8C73-4835-B57E-A52C99FE46FC",
                    "PWNumber": "0339656",
                    "SerialNumberTime": "2022-09-25",
                    "SupplierNameId": "",
                    "SupplierName": "",
                    "TotalAmount": 103.6941,
                    "TaxiAmount": 94.2674,
                    "Status": ""
                }
            ]
        })
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurcWarehousingDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "2CDD5D28-8C73-4835-B57E-A52C99FE46FC",
                    "PWNumber": "0339656",
                    "Psn": "90227378",
                    "Quantity": 10,
                    "QuantityReal": 10,
                    "BuyCount": 10,
                    "Price": 13.15,
                    "PriceTaxi": 14.728,
                    "TaxRate": 12,
                    "DrugsBase_DrugName": "尿素维E乳膏",
                    "DrugsBase_Specification": "40g",
                    "DrugsBase_Manufacturer": "上海中华药业南通有限公司",
                    "ApprovalNumber": "",
                    "Stock_Unit": "",
                    "Valuation_Unit": "",
                    "Valuation_Number": 9,
                    "Buy_Unit": "",
                    "Spxq": "",
                    "YouXq": "",
                    "BatchPurchasePrice_Detail": 11
                }
            ]
        })
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main.text, response_detail.text
    elif type == '采购退货单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseReturnedByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "35A3203A-981D-4585-8B9A-6E5FC60C3B29",
                    "PRNumber": "1D627B6",
                    "SerialNumberTime": "2022-09-25",
                    "SupplierNameId": "",
                    "SupplierName": "",
                    "Status": ""
                }
            ]
        }
        )
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseReturnedDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "35A3203A-981D-4585-8B9A-6E5FC60C3B29",
                    "PRNumber": "1D627B6",
                    "Psn": "90227378",
                    "RebateCount": 4,
                    "Price": 50,
                    "PriceTaxi": 53,
                    "TaxRate": 6,
                    "DrugsBase_DrugName": "",
                    "DrugsBase_Specification": "",
                    "DrugsBase_Manufacturer": "",
                    "ApprovalNumber": "",
                    "Buy_Unit": "",
                    "BatchPurchasePrice_Detail": 53
                }
            ]
        })
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main.text, response_detail.text
    elif type == '付款单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/ReceiptByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "F2D5B59F-5195-4DF8-B686-F1CC52A9B500",
                    "RNumber": "DD98FC4",
                    "SerialNumberTime": "2022-08-25",
                    "SupplierNameId": "12",
                    "SupplierName": "12",
                    "SupplierType": "12",
                    "AmountsPayable": 778.4,
                    "AmountActually": 778.4,
                    "PaymentPurpose": "12",
                    "SettlementMethod": "12"
                }
            ]
        })
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/ReceiptDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "F2D5B59F-5195-4DF8-B686-F1CC52A9B500",
                    "RNumber": "DD98FC4",
                    "Number": "",
                    "Remk": ""
                }
            ]
        }
        )
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main.text, response_detail.text


if __name__ == '__main__':
    print(send(type="批发销售单"))
