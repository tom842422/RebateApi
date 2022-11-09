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
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail
    elif type == '零售销售单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/RetailSalesOrderByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C2",
                    "RSONumber": "E381DB0",
                    "SerialNumberTime": "2022-08-25",
                    "SalesOrganizationNo": "sc0001",
                    "SalesOrganization": "成都青羊店",
                    "SalesOrganizationType": "0",
                    "Customer": "soso",
                    "Seller": "ZW",
                    "Status": ""
                }
            ]
        })
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/RetailSalesOrderDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "0CD68119-6980-4394-8ABE-D1A78089BE5C22",
                    "RSONumber": "E381DB0",
                    "Psn": "751568",
                    "Quantity": 100,
                    "Price": 10,
                    "PriceTaxi": 12,
                    "TaxRate": 20,
                    "DrugsBase_DrugName": "阿昔洛韦乳膏",
                    "DrugsBase_Specification": "10g:0.3g",
                    "DrugsBase_Manufacturer": "福建太平洋制药有限公司",
                    "ApprovalNumber": "",
                    "VenderErpId": "3332",
                    "VenderErpName": "广东壹号药业有限公司",
                    "VenderErpType": "",
                    "GiftSign_Detail": "free",
                    "BatchPurchasePrice_Detail": 11.5
                }
            ]
        }
        )
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail
    elif type == '配送出库单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseDeliveryByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "822777EB-701A-4169-946C-B5F183EC5034",
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
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseDeliveryDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "822777EB-701A-4169-946C-B5F183EC5034",
                    "DeliNumber": "996DFC5",
                    "Psn": "56694",
                    "QuantityReal": 70,
                    "Quantity": 70,
                    "BuyCount": 70,
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
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail
    elif type == '采购入库单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurcWarehousingByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "2CDD5D28-8C73-4835-B57E-A52C99FE46FC",
                    "PWNumber": "0339656",
                    "SerialNumberTime": "2022-08-25",
                    "SupplierNameId": "",
                    "SupplierName": "",
                    "TotalAmount": 103.6941,
                    "TaxiAmount": 94.2674,
                    "Status": ""
                }
            ]
        })
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurcWarehousingDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "2CDD5D28-8C73-4835-B57E-A52C99FE46FC",
                    "PWNumber": "0339656",
                    "Psn": "14283",
                    "Quantity": 80,
                    "QuantityReal": 80,
                    "BuyCount": 80,
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
                    "BatchPurchasePrice_Detail": 235.6685
                }
            ]
        })
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail
    elif type == '采购退货单':
        url_main = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseReturnedByJson"
        payload_main = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "35A3203A-981D-4585-8B9A-6E5FC60C3B19",
                    "PRNumber": "1D627B6",
                    "SerialNumberTime": "2022-08-25",
                    "SupplierNameId": "",
                    "SupplierName": "",
                    "Status": ""
                }
            ]
        }
        )
        url_detail = "http://192.168.1.12:9999/Api/RebateAgreementSaveBillDataByJson/PurchaseReturnedDetailByJson"
        payload_detail = json.dumps({
            "secretKey": "123456",
            "data": [
                {
                    "id": "35A3203A-981D-4585-8B9A-6E5FC60C3B19",
                    "PRNumber": "1D627B6",
                    "Psn": "14283",
                    "RebateCount": 100,
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
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail
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
        response_main = requests.request(
            "POST", url=url_main, headers=header, data=payload_main)
        response_detail = requests.request(
            "POST", url_detail, headers=header, data=payload_detail)
        return response_main, response_detail


if __name__ == '__main__':
    print(send(type="批发销售单"))
