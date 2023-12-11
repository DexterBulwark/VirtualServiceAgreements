# Virtual Service Agreement

This repository contains examples of the expected JSON to receive for service agreements and the HTML that it should be converted to. It also contains examples of how the fine print should be given when requested through an API.

## Rules

### Optional Fields
The majority of fields must be required in the JSON when accepting a service agreement. The only fields that are not required are:

**ALL**
- `billingInfo` (default to customer info if not provided)
- `savedOn` (this should be filled on our end when the json is received)

**GENERAL PEST**
- `services->recurring` (would not be needed for One Time Treatments)

<br>

<details>
<summary>Addition notes on optional fields</summary>
<br>

*Technically any service field could be optional but there will always be an initial service as this would just be the first/only service they receive.*

*It should be safe to just build in that if there is any service found in the JSON that it is a valid service agreement and should be saved and processed.*

</details>

### Service Lists
All `initial services` and `recurring services` are list and can have any number of items. They will always need to follow the following format:




**Initial Service** *(Termite Protection, Initial Warranty Extension)*
```json
"initial": [
    {
        "name": "",
        "price": 0.0
    }
],
```

**Recurring Service** *(Recurring Termite Services, Recurring Warranty Extension)*

```json
"recurring": [
    {
        "name": "",
        "price": 0.0,
        "frequency": ""
    }
],
```

And should be inserted in the HTML like this:

**Initial Service**
```html
<li>
    <span class="service-name">{{serviceName}}</span>
    <span class="service-cost">${{serviceCost}}</span>
</li>
```
**Recurring Service**
```html
<li>
    <span class="service-name">{{serviceName}}</span>
    <span class="service-cost">${{serviceCost}} <i>({{paymentFrequency}})</i></span>
</li>

```

<details>
<summary>Examples with multiple services</summary>

```json
"recurring": [
    {
        "serviceName": "Pest Control",
        "serviceCost": 56.00,
        "paymentFrequency": "Monthly"
    },
    {
        "serviceName": "Rodent Control",
        "serviceCost": 60.00,
        "paymentFrequency": "Per Service"
    }

],
```

```html
<li>
  <span class="service-name">Pest Control</span>
  <span class="service-cost">$56.00 <i>(Monthly)</i></span>
</li>
<li>
  <span class="service-name">Rodent Control</span>
  <span class="service-cost">$60.00 <i>(Per Service)</i></span>
</li>
```
</details>

### Fine Print 

The fine print will be returned like so:

```JSON
"finePrint":
    [
        "5",
        "7",
        "13",
        "8",
        "9"
    ],
```

Each number would represent the Id of the fine print content used. 

<details>
<summary>Note</summary>

The contents can be found in the ServiceAgreementFinePrintContent table. For testing purposes you can use any numbers between 3 and 37 at this time 

</details>

### Signature

The signature should be received as a **base64** encoded image which will be converted on our end and placed into the signature section. 

The image should be a **3000x500** image (JPG, JPEG, PNG, PDF). The dimensions should be maintained for consistency. 

### Times

All times should be in UTC time. The one exception being the `initialServiceDate` and `initialServiceTime`. These fields should be expected as a string and look like this:

```json
"initialServiceDate": "Jan 02, 2024",
"initialServiceTime": "1:00PM - 4:00PM",
```

<details>
<summary>Filled Out JSON Timestamp Section </summary>
<br>

```json
"timestamps": 
{
    "createdOn": "2023-11-08T22:33:22.358Z",
    "openedOn": "2023-11-08T22:34:22.358Z",
    "signedOn": "2023-11-08T22:46:22.358Z",
    "submittedOn": "2023-11-08T22:46:52.358Z",
    "savedOn": "2023-11-08T22:46:52.358Z"
}
```
</details>


## API Request

***Both of the APIs should have some level of security,even if it is just basic auth.***

### Accept Service Agreements ***(do this first)***

Please build an API that is able to take in the raw JSON, plug in the information to the corresponding HTML template, and save the filled out HTML as a uneditable PDF.

This API should be well documented. We would like to be able to provide the documentation to 3rd parties so they can communicate to this API with their own systems. The documentation should include what the API expects to receive, the possible responses that the sender should expect, and any other important information.


<details>
<summary>Templates</summary>

**General Pest**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/templates/general_pest.json)

- [HTML](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/templates/generalPest.html)

**Termite Control**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/templates/termite_control.json)

- [HTML](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/templates/termiteControl.html)

**Termite Warranty**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/templates/termite_warranty.json)

- [HTML](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/templates/termiteWarranty.html)

</details>

<br>

<details>
<summary>Filled Out Examples</summary>

**General Pest**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/examples/general_pest.json)

- [HTML](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/generalPest.html)

- [PDF](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/pdfExamples/generalPest.pdf)

**Termite Control**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/examples/termite_control.json)

- [HTML](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/termiteControl.html)

- [PDF](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/pdfExamples/termiteControl.pdf)

**Termite Warranty**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/examples/termite_warranty.json)

- [HTML](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/termiteWarranty.html)

- [PDF](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/pdfExamples/termiteWarranty.pdf)

</details>


### Provide Fine Print ***(do not do this yet)***

Create an API that will accept an office id and return all of the fine print for that office among other information. 

This API should be well documented. We would like to be able to provide the documentation to 3rd parties so they can communicate to this API with their own systems. The documentation should include how to call the API, the possible responses that the sender should expect, and any other important information.

<details>
<summary>Examples</summary>

Empty JSON
``` json
{
    "officeId": 0,
    "officeName": "",
    "streetAddress": "",
    "city": "",
    "state": "",
    "zip": "",
    "phoneNumber": "",
    "licenses": {
        "": {
            "generalPest": "",
            "termite": "",
            "lawnAndWeed": ""
        }
    },
    "finePrintContentOrder": [
        {
            "": ""
        }
    ],
    "finePrintContent": {
        "": {
            "": ""
        }
    },
    "finePrintContentRules": {
        "": {
            "include": {
                "": [
                    {
                        "office": "",
                        "stateCode": "",
                        "isBuilder": "",
                        "category": "",
                        "serviceType": "",
                        "include": ""
                    }
                ]
            },
            "exclude": {
                "": [
                    {
                        "office": "",
                        "stateCode": "",
                        "isBuilder": "",
                        "category": "",
                        "serviceType": "",
                        "include": ""
                    }
                ]
            }
        }
    }
}
```

<details>
<summary>Filled JSON</summary>

``` json
{
    "officeId": 7,
    "officeName": "Saint George",
    "streetAddress": "56 North 500 East",
    "city": "Saint George",
    "state": "UT",
    "zip": "84770",
    "phoneNumber": "(435) 627-8840",
    "licenses": {
        "UT": {
            "generalPest": "4000-467",
            "termite": "4000-467",
            "lawnAndWeed": "4000-467"
        },
        "NV": {
            "generalPest": "5253",
            "termite": "5253",
            "lawnAndWeed": "5253"
        },
        "AZ": {
            "generalPest": "5632",
            "termite": "5632",
            "lawnAndWeed": "5632"
        }
    },
    "finePrintContentOrder": [
        {
            "2": "Bulwark is hereby authorized..."
        },
        {
            "3": "Important: Customer Understand..."
        },
        {
            "6": "BULWARK PROPERTY"
        }
    ],
    "finePrintContent": {
        "Bulwark is hereby authorized...": {
            "4": "BULWARK is hereby authorized to install bait stations in and around Customer's premises on the Installation Date Range listed on this AGREEMENT. Prior to Installation, BULWARK will provide Customer a Subterranean Termite Post-Construction Treatment Estimate / Disclosure Document."
        },
        "Important: Customer Understand...": {
            "5": "IMPORTANT: Customer understands that BULWARK will not be responsible for repairs or replacement of damaged material to any structure situated on Customer's premises or their contents caused by Subterranean Termites or other wood destroying organisms. The term “Service” or “Services” under this Agreement means the bait station program, and Guarantee set forth below. If during the effective period of this Agreement, BULWARK, for whatever reason, changes the type of bait being used or ceases to offer a bait program in Customer's area, an appropriate alternative treatment method, if available, will be determined by and performed by BULWARK at no additional charge to Customer. The bait stations and all components are owned at all times by BULWARK and may be removed at any time by BULWARK at its discretion, (i) for replacement with an alternative treatment method, (ii) upon the termination of this Agreement; or, (iii) if BULWARK ceases to offer a bait program in this Customer's area. BULWARK'S Services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any and all claims of liability for personal injury and/or property damage resulting from the Services performed, by Bulwark including damages to Customer's home, other structures, or their contents, whether preexisting or after the Services are performed, caused by an infestation of, or damage resulting from Subterranean Termites (including Formosan Termites), Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. Customer shall receive the following Retreatment Guarantee after the installation of the bait stations and payment.",
            "6": "IMPORTANT: Customer understands that BULWARK will not be responsible for repairs or replacement of damaged material to any structure situated on Customer's premises or their contents caused by Subterranean Termites or other wood destroying organisms. The term “Service” or “Services” under this Agreement means the Bulwark Retreatment Guarantee set forth below. BULWARK'S Retreatment Guarantee and Services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any and all claims of liability for personal injury and/or property damage resulting from the Services performed, by Bulwark including damages to Customer's home, other structures, or their contents, whether preexisting or after the Services are performed, caused by an infestation of, or damage resulting from Subterranean Termites (including Formosan Termites), Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. The following Retreatment Guarantee shall be effective upon payment of the above Retreatment Guarantee Fees and/or payment of $1.00 to initiate this AGREEMENT."
        },
        "BULWARK PROPERTY": {
            "14": "Any bait stations, equipment or devices placed or installed at the Customer's property are not owned by the Customer and may be removed by BULWARK at its discretion, at any time, for any reason, including, but not limited to replacement with an alternative treatment method, as a practice of Integrated Pest Management, or upon the termination of this Agreement. Virtually all pesticides have some odor which may be present for a short while after application. If you or any member of your household has a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have your home serviced for pest control until you have consulted your family physician. All technicians are licensed and bonded. You, the customer, may cancel this transaction at any time prior to midnight of the third business day after the date of this transaction."
        }
    },
    "finePrintContentRules": {
        "Bulwark is hereby authorized...": {
            "include": {
                "4": [
                    {
                        "office": "Saint George",
                        "stateCode": "AZ",
                        "isBuilder": "False",
                        "category": "General Pest",
                        "serviceType": "5 Treatment Program",
                        "include": "True"
                    },
                    {
                        "office": "Saint George",
                        "stateCode": "UT",
                        "isBuilder": "True",
                        "category": "General Pest",
                        "serviceType": "5 Treatment Program",
                        "include": "True"
                    }
                ]
            },
            "exclude": {}
        },
        "Important: Customer Understand...": {
            "include": {
                "5": [
                    {
                        "office": "Saint George",
                        "stateCode": "AZ",
                        "isBuilder": "True",
                        "category": "General Pest",
                        "serviceType": "5 Treatment Program",
                        "include": "True"
                    }
                ],
                "6": [
                    {
                        "office": "Saint George",
                        "stateCode": "AZ",
                        "isBuilder": "False",
                        "category": "General Pest",
                        "serviceType": "Gopher Control Additional",
                        "include": "True"
                    }
                ]
            },
            "exclude": {}
        },
        "BULWARK PROPERTY": {
            "include": {
                "14": [
                    {
                        "office": "",
                        "stateCode": "",
                        "isBuilder": "",
                        "category": "",
                        "serviceType": "",
                        "include": "True"
                    }
                ]
            },
            "exclude": {
                "14": [
                    {
                        "office": "Saint George",
                        "stateCode": "",
                        "isBuilder": "",
                        "category": "",
                        "serviceType": "",
                        "include": "False"
                    }
                ]
            }
        }
    }
}
```
</details>
</details>

<details>
<summary>Example API</summary>

Here is an example of a function API that does this. The API is written in Python and should not be used in production. For speed, reliability, and consistency we would like for it to be written in PHP. Please reach out to dexterd@bulwarkpest.com if you would like the raw Python code.

The API can be used [HERE](https://api-tools.tem-pest.com/v1/requestServiceAgreementsInfo?officeId=7)

Interactive documentation can be found [HERE](https://api-tools.tem-pest.com/v1/docs#/Service%20Agreement/request_service_agreement_requestServiceAgreementsInfo_get)


</details>