# Virtual Service Agreement

This repository contains examples of the expected JSON to receive for service agreements and the HTML that it should be converted to. It also contains examples of how the fine print should be given when requested through an API.


[Service Agreement Samples](https://admin.tem-pest.com/serviceAgreements/samples/generalPest.html)


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
The Services will be returned like this. The naming conventions can change between contracts. Please refer to the [samples](https://admin.tem-pest.com/serviceAgreements/samples/generalPest.html) for the most accurate naming conventions:

```json
"services": 
    {
        "initialWarrantyExtension": 
        [
            {
                "name": "",
                "description": "",
                "price": 0.0
            }
        ],
        "initialTotalPrice": 0.0,
        "recurringWarrantyExtension":
        {
            "monthly": 
            [
                {
                    "name": "",
                    "description": "",
                    "price": 0.0
                }
            ],
            "perService": 
            [
                {
                    "name": "",
                    "description": "",
                    "price": 0.0
                }
            ]
        },
        "recurringMonthlyTotalPrice": 0.0,
        "recurringPerServiceTotalPrice": 0.0
    },
```

### Fine Print 

The fine print will be returned like so:

```JSON
"finePrint": 
    [
        {
            "title": "",
            "content": "",
            "style": ""
        }
    ],
```

### Signature

The signature should be received as a **base64** encoded image which will be converted on our end and placed into the signature section. 

The image should be a **3000x500** image (JPG, JPEG, PNG, PDF). The dimensions should be maintained for consistency. 

### Timestamps

All times should be in UTC time. The one exception being the `initialServiceDate` and `initialServiceTime` (These fields can be found in the treatmentInfo. Is not found in all service agreements). These fields should be expected as a string and look like this:

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

<br>

**ALL TEMPLATES CAN BE FOUND [HERE](https://admin.tem-pest.com/serviceAgreements/samples/generalPest.html)**

<br>


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
    "state": {
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
      "": {
        "content": "",
        "": ""
      }
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
            "serviceType": ""
          
          }
        ]
      },
      "exclude": [
        {
            "office": "",
            "stateCode": "",
            "isBuilder": "",
            "category": "",
            "serviceType": ""
          
          }
      ]
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
      "1": "ADDENDUM"
    },
    {
      "2": "Bulwark is hereby authorized..."
    },
    {
      "3": "IMPORTANT"
    },
    {
      "4": "Because most infestations start outside..."
    },
    {
      "5": "RENEWABLE SUBTERRANEAN TERMITE RETREATMENT GUARANTEE"
    },
    {
      "6": "BULWARK PROPERTY"
    },
    {
      "7": "CUSTOMER'S OBLIGATIONS TO MAINTAIN RETREATMENT GUARANTEE"
    },
    {
      "8": "PAYMENTS"
    },
    {
      "9": "LATE PAYMENT"
    },
    {
      "10": "REINSPECTION"
    },
    {
      "11": "SERVICE EXCLUSION, WAIVER, AND RELEASE"
    },
    {
      "12": "ARBITRATION"
    },
    {
      "13": "LIMITATION OF LIABILITY"
    },
    {
      "14": "SERVICE TO BE PROVIDED"
    },
    {
      "15": "TRANSFER"
    },
    {
      "16": "CHEMICAL SENSITIVITY"
    },
    {
      "17": "AGREEMENT"
    },
    {
      "18": "FORCE MAJEURE (Circumstances beyond BULWARK'S control)"
    },
    {
      "19": "TERMINATION"
    },
    {
      "20": "Consumer Information Sheet"
    },
    {
      "21": "The Georgia Structural Pest Con..."
    }
  ],
  "finePrintContent": {
    "Because most infestations start outside...": {
      "3": {
        "content": "BECAUSE MOST INFESTATIONS START OUTSIDE, BULWARK'S SYSTEM IS DESIGNED TO MAINTAIN A STRONG EXTERIOR BARRIER WHICH IS REINFORCED ON A REGULAR BASIS. SHOULD INSIDE SERVICE BE REQUIRED, PLEASE FEEL FREE TO CONTACT US FOR AN INSIDE VISIT AT NO EXTRA CHARGE. IF SERVICE IS CANCELED PRIOR TO THE LENGTH OF AGREEMENT, THE CUSTOMER AGREES TO PAY ANY DISCOUNTS RECEIVED ON THE INITIAL SERVICE.",
        "style": "bold"
      }
    },
    "Bulwark is hereby authorized...": {
      "4": {
        "content": "BULWARK is hereby authorized to install bait stations in and around Customer's premises on the Installation Date Range listed on this AGREEMENT. Prior to Installation, BULWARK will provide Customer a Subterranean Termite Post-Construction Treatment Estimate / Disclosure Document.",
        "style": "bold"
      }
    },
    "IMPORTANT": {
      "5": {
        "content": "Customer understands that BULWARK will not be responsible for repairs or replacement of damaged material to any structure situated on Customer's premises or their contents caused by Subterranean Termites or other wood destroying organisms. The term “Service” or “Services” under this Agreement means the bait station program, and Guarantee set forth below. If during the effective period of this Agreement, BULWARK, for whatever reason, changes the type of bait being used or ceases to offer a bait program in Customer's area, an appropriate alternative treatment method, if available, will be determined by and performed by BULWARK at no additional charge to Customer. The bait stations and all components are owned at all times by BULWARK and may be removed at any time by BULWARK at its discretion, (i) for replacement with an alternative treatment method, (ii) upon the termination of this Agreement; or, (iii) if BULWARK ceases to offer a bait program in this Customer's area. BULWARK'S Services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any and all claims of liability for personal injury and/or property damage resulting from the Services performed, by BULWARK including damages to Customer's home, other structures, or their contents, whether preexisting or after the Services are performed, caused by an infestation of, or damage resulting from Subterranean Termites (including Formosan Termites), Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. Customer shall receive the following Retreatment Guarantee after the installation of the bait stations and payment.",
        "style": ""
      },
      "6": {
        "content": "Customer understands that BULWARK will not be responsible for repairs or replacement of damaged material to any structure situated on Customer's premises or their contents caused by Subterranean Termites or other wood destroying organisms. The term “Service” or “Services” under this Agreement means the BULWARK Retreatment Guarantee set forth below. BULWARK'S Retreatment Guarantee and Services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any and all claims of liability for personal injury and/or property damage resulting from the Services performed, by BULWARK including damages to Customer's home, other structures, or their contents, whether preexisting or after the Services are performed, caused by an infestation of, or damage resulting from Subterranean Termites (including Formosan Termites), Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. The following Retreatment Guarantee shall be effective upon payment of the above Retreatment Guarantee Fees and/or payment of $1.00 to initiate this AGREEMENT.",
        "style": ""
      },
      "7": {
        "content": "Customer understands that BULWARK will not be responsible for repairs or replacement of damaged material to the structure or its contents caused by Subterranean Termites or other wood destroying organisms. If during the effective period of this agreement, BULWARK, for whatever reason, changes the type of bait being used or ceases to offer a bait program in this area, if available, an appropriate alternative treatment method will be determined by and performed by BULWARK. Any bait stations, equipment or devices placed or installed at the Customer's property are not owned by the Customer and may be removed by BULWARK at its discretion, at any time, for any reason, including, but not limited to; replacement with an alternative treatment method, as a practice of Integrated Pest Management, or upon the termination of this Agreement, or, if BULWARK ceases to offer a bait program in this area. Service includes Bait System installation and Warranty as specified by BULWARK. BULWARK'S services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any liability for any claim for personal injury resulting from the services performed, under this contract, or damages to the structure or its contents whether preexisting or after the services are performed, caused by an infestation of Formosan Termites, Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. Customer shall receive the following Guarantee after the initial service is performed.",
        "style": ""
      }
    },
    "AGREEMENT": {
      "8": {
        "content": "This Agreement shall be the entire Agreement between Customer and BULWARK for the Services. The terms and the guarantee stated in this Agreement may not be amended or altered unless a written change is approved and signed by The Director of Operations of BULWARK EXTERMINATING, LLC.",
        "style": ""
      }
    },
    "ARBITRATION": {
      "11": {
        "content": "Any dispute arising out of or relating to this agreement or the services performed under this agreement or tort based claims for personal or bodily injury or damage to real or personal property shall be finally resolved by arbitration administered under the Commercial Arbitration rules of the American Arbitration Association. This agreement involves interstate commerce; furthermore, the parties expressly agree that their mutual rights and obligations under the conduct of any arbitration proceeding shall be controlled by the Federal Arbitration Act. The award of the arbitrator shall be final, binding, non-appealable and may be entered and enforced in any court having jurisdiction in accordance with the Federal Arbitration Act. The arbitrator shall not have the power or authority to award exemplary, treble, liquidated or any type of punitive damages.",
        "style": ""
      }
    },
    "BULWARK PROPERTY": {
      "13": {
        "content": "Any bait stations, equipment or devices placed or installed at the Customer's property are not owned by the Customer and may be removed by BULWARK at its discretion, at any time, for any reason, including, but not limited to replacement with an alternative treatment method, as a practice of Integrated Pest Management, or upon the termination of this Agreement.",
        "style": ""
      }
    },
    "CHEMICAL SENSITIVITY": {
      "15": {
        "content": "At times additional termiticides may be used to control termites. These additional termiticides may have some odor which may be present for a short time after application. If you or any member of your household believes you have a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have any Services performed at your premises until you have consulted with your family physician. At your request, Bulwark will provide information about the chemicals to be used in treating the premises.",
        "style": ""
      },
      "16": {
        "content": "Virtually all pesticides have some odor which may be present for a short while after application. If you or any member of your household has a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have your home serviced for pest control until you have consulted your family physician.",
        "style": ""
      }
    },
    "Consumer Information Sheet": {
      "17": {
        "content": "https://bulwarkpestcontrol.com/txconsumerinfo",
        "style": ""
      }
    },
    "CUSTOMER'S OBLIGATIONS TO MAINTAIN RETREATMENT GUARANTEE": {
      "18": {
        "content": "Customer agrees not to remove, tamper with, or cover bait stations. Customer shall make the premises and structure(s) on premises available to BULWARK for inspections and treatments, either liquid or bait as BULWARK deems necessary, which may include the removal of floor coverings, wall coverings and fixtures. Failure to honor the requirements to maintain the structure or to allow BULWARK access for inspections or treatments as appropriate will void the Retreatment Guarantee.",
        "style": ""
      },
      "19": {
        "content": "Customer shall make the premises and structure(s) on premises available to BULWARK for inspections and treatments, as BULWARK deems necessary, which may include the removal of floor coverings, wall coverings and fixtures. Failure to honor the requirements to maintain the structure or to allow BULWARK access for inspections or treatments as appropriate will void the Retreatment Guarantee.",
        "style": ""
      }
    },
    "FORCE MAJEURE (Circumstances beyond BULWARK'S control)": {
      "20": {
        "content": "BULWARK'S obligations under this Agreement shall be suspended or canceled if Bulwark is unable to perform its responsibilities due to a substantial change of circumstances, including, but not limited to acts of war, strikes, pandemics, unavailability of termiticides, or other supplies from ordinary sources, or if acts of God or natural occurrences, such as earthquakes, storms, fires and floods substantially alters or destroys the effectiveness of Bulwark's treatment.",
        "style": ""
      }
    },
    "LATE PAYMENT": {
      "21": {
        "content": "If the customer fails, for any reason to make a monthly payment within 30 days from the due date, Bulwark, at its option may discontinue the service and start collection proceedings. Upon failure to make such payments, the customer agrees to pay all costs of collecting, including a reasonable attorney's fee.",
        "style": ""
      },
      "22": {
        "content": "If the customer fails, for any reason, to make a payment within 30 days from the due date, Bulwark, at its option, may start collection proceedings. Upon failure to make such payments, the customer agrees to pay all costs of collecting, including a reasonable attorney's fee.",
        "style": ""
      }
    },
    "LIMITATION OF LIABILITY": {
      "23": {
        "content": "Customer waives any claims for personal injury and/or property damages related to the Services BULWARK performs under this Agreement. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises while treating their structures, including any damage to shrubs, trees, or plants. The Services performed by BULWARK may include drilling into soil, through concrete or the structure itself. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises as a result of drilling, including but not limited to damage caused to plumbing or electrical pipes, wires, or conduits. To avoid potential damage, customer is advised to use a utility locating service to identify the location of the utility lines in or near the structures prior to BULWARK'S Services. When performing the Services, it may be necessary for Customer to remove floor coverings, floors, excavate crawl spaces and provide access to walls, ceilings, or floors. Customer shall be responsible for the cost of dismantling and reconstruction of any item required in order to provide adequate access for providing Services. Customer acknowledges that modifications or alterations to the structure during this agreement may void this Retreatment Guarantee. Customer is advised to notify BULWARK in advance to determine whether such modifications or alterations will void the Retreatment Guarantee or if additional Services will be required at an additional cost to the Customer in order to validate the Retreatment Guarantee. Customer expressly waives and releases BULWARK from and against any claims for (a) loss of use or diminution of property value, (b) economic, compensatory, incidental, or consequential damages and/or (c) exemplary or punitive damages. Customer further agrees that under no circumstances shall BULWARK be liable for any amount greater than the amount paid by Customer to BULWARK for the Services performed.",
        "style": ""
      }
    },
    "PAYMENTS": {
      "27": {
        "content": "Your payment of the Retreatment Guarantee Fee extends subterranean termite protection for work performed by BULWARK during the construction of your home. At the end of Bulwark's Guarantee Expiration Date this agreement automatically renews on a month-to-month basis. So long as the Retreatment Guarantee Fee is paid when due, BULWARK will honor the Retreatment Guarantee.",
        "style": ""
      }
    },
    "REINSPECTION": {
      "28": {
        "content": "BULWARK shall reinspect the treated structures on Customer's premises as deemed necessary by BULWARK or as requested by Customer.",
        "style": ""
      },
      "29": {
        "content": "BULWARK shall reinspect the treated structures on Customer's premises as deemed necessary by BULWARK or as requested by Customer. The frequency of these inspections shall be in accordance with the Trelona ATBS product label.",
        "style": ""
      }
    },
    "RENEWABLE SUBTERRANEAN TERMITE RETREATMENT GUARANTEE": {
      "30": {
        "content": "So long as Customer complies with the Customer obligations below, and provided that all payments including guarantee fees are current, if Bulwark is notified that an infestation of Subterranean Termites has been found, Bulwark will, on inspection, either retreat the structure for Subterranean Termites at no additional cost to the Customer or Customer may cancel this agreement and Bulwark will refund Customer's installation charges. CUSTOMER EXPRESSLY RELEASES BULWARK FROM ANY AND ALL CLAIMS FOR PERSONAL INJURY, PROPERTY DAMAGE, AND FOR SUBTERRANEAN TERMITE DAMAGE OR REPAIR.",
        "style": ""
      },
      "31": {
        "content": "So long as Customer complies with the Customer obligations below, and provided that all payments of the applicable Retreatment Guarantee Fees are current, if Bulwark is notified that an infestation of Subterranean Termites has been found, Bulwark will, on inspection, either retreat the structure for Subterranean Termites, at no additional cost to the Customer, or Customer may cancel this agreement. CUSTOMER EXPRESSLY RELEASES BULWARK FROM ANY AND ALL CLAIMS FOR PERSONAL INJURY, PROPERTY DAMAGE, AND FOR SUBTERRANEAN TERMITE DAMAGE OR REPAIR.",
        "style": ""
      }
    },
    "SERVICE EXCLUSION, WAIVER, AND RELEASE": {
      "32": {
        "content": "I understand that this agreement does not include the control or prevention of wood infesting organisms such as termites, powder post beetles, wood borers, carpenter ants, carpenter bees, wood wasps, or wood decay fungus. I expressly waive and release Bulwark from liability for any claim for personal injury or damages to the structure or its content caused by wood infesting organisms. I also waive any claims in any lawsuit, arbitration, or legal proceeding against Bulwark for (a) loss of use or diminution of value, (b) economic, compensatory, incidental, or consequential damages of any kind, or (c) exemplary or punitive damages.",
        "style": ""
      },
      "33": {
        "content": "I understand that this agreement does not include the control or prevention of wood infesting organisms such as termites, powder post beetles, wood borers, wood wasps, or wood decay fungus. I understand that this agreement does not include the control or prevention of bedbugs. I expressly waive and release Bulwark from liability for any claim for personal injury or damages to the structure or its content caused by wood infesting organisms, fire ants, pharaoh ants, spiders, ticks, wasps, bees or other pests listed in this agreement. I also waive any claims in any lawsuit, arbitration or legal proceeding against Bulwark for (a) loss of use or diminution of value, (b) economic, compensatory, incidental, or consequential damages of any kind, or (c) exemplary or punitive damages.",
        "style": ""
      }
    },
    "SERVICE TO BE PROVIDED": {
      "34": {
        "content": "After the initial length of agreement, this agreement is automatically renewable on a month to month basis and may be cancelled anytime after the length of agreement by either party giving 30 days written notice.",
        "style": ""
      }
    },
    "TERMINATION": {
      "35": {
        "content": "BULWARK may terminate this Agreement, including the Guarantee and any renewal rights, contained herein, if Customer does not meet its payment or other Customer obligations, or in the event of a change in state, federal, or local law that substantially affects BULWARK'S obligations under this Agreement. Customer may cancel this agreement at any time prior to midnight of the third business day after the date of this transaction. After midnight of the third business day after the date of this transaction, either party may cancel this agreement giving 30 days written notice to the other party. Any amounts due and unpaid under this Agreement are subject to late fees of ten percent (10%) of the unpaid amount and interest at the rate of ten percent (10%) per annum, as well as attorney fees and collection costs whether or not suit is brought.",
        "style": ""
      }
    },
    "TRANSFER": {
      "37": {
        "content": "This Agreement is transferable to a new property owner upon written notice to BULWARK and new owner's assumption of the Retreatment Guarantee fee.",
        "style": ""
      }
    },
    "The Georgia Structural Pest Con...": {
      "38": {
        "content": "The Georgia Structural Pest Control Act requires all pest control companies to maintain insurance coverage. Information about this coverage is available from this pest control company.",
        "style": "bold"
      },
      "39": {
        "content": "The Georgia Structural Pest Control Act requires all pest control companies to maintain insurance coverage. Information about this coverage is available from this pest control company. In accordance with state regulations, pest control companies have a responsibility to provide you with a record every time a pesticide product and/or pest system is applied. This record is required to be provided to the property owner, resident or custodian of the property. This record may include post-application precautionary information. Licensed and regulated by the Georgia Department of Agriculture, 19 Martin Luther King, Jr. Drive, Atlanta, Georgia 30334 (404) 656-3641. I understand and request that my pesticide use records be provided or made available to me electronically.",
        "style": "bold"
      }
    },
    "ADDENDUM": {
      "40": {
        "content": "This document is an addendum to the original service agreement between the Customer and Bulwark Exterminating and may not represent all services Bulwark performs for the Customer.",
        "style": ""
      }
    }
  },
  "finePrintContentRules": {
    "Because most infestations start outside...": {
      "include": {
        "3": [
          {
            "category": "General Pest"
          }
        ]
      },
      "exclude": []
    },
    "Bulwark is hereby authorized...": {
      "include": {
        "4": [
          {
            "category": "Termite Control",
            "serviceType": "Termite Bait Station 1"
          },
          {
            "category": "Termite Control",
            "serviceType": "Termite Bait Station Formosan 1"
          }
        ]
      },
      "exclude": []
    },
    "IMPORTANT": {
      "include": {
        "5": [
          {
            "isBuilder": "True",
            "category": "Termite Control",
            "serviceType": "Termite Bait Station 1"
          },
          {
            "isBuilder": "True",
            "category": "Termite Control",
            "serviceType": "Termite Bait Station Formosan 1"
          }
        ],
        "6": [
          {
            "isBuilder": "True",
            "category": "Termite Control"
          }
        ],
        "7": [
          {
            "isBuilder": "False",
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "AGREEMENT": {
      "include": {
        "8": [
          {
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "ARBITRATION": {
      "include": {
        "11": [
          {}
        ]
      },
      "exclude": []
    },
    "BULWARK PROPERTY": {
      "include": {
        "13": [
          {
            "category": "General Pest"
          }
        ]
      },
      "exclude": []
    },
    "CHEMICAL SENSITIVITY": {
      "include": {
        "15": [
          {
            "category": "Termite Control"
          }
        ],
        "16": [
          {}
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "Consumer Information Sheet": {
      "include": {
        "17": [
          {
            "stateCode": "TX"
          }
        ]
      },
      "exclude": []
    },
    "CUSTOMER'S OBLIGATIONS TO MAINTAIN RETREATMENT GUARANTEE": {
      "include": {
        "18": [
          {
            "isBuilder": "True",
            "category": "Termite Control",
            "serviceType": "Termite Bait Station 1"
          },
          {
            "isBuilder": "True",
            "category": "Termite Control",
            "serviceType": "Termite Bait Station Formosan 1"
          }
        ],
        "19": [
          {
            "isBuilder": "False",
            "category": "Termite Control"
          },
          {
            "isBuilder": "True",
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "FORCE MAJEURE (Circumstances beyond BULWARK'S control)": {
      "include": {
        "20": [
          {
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "LATE PAYMENT": {
      "include": {
        "21": [
          {
            "category": "General Pest"
          }
        ],
        "22": [
          {
            "category": "Termite Control",
            "serviceType": "Termite Inspection - Termite Account"
          },
          {
            "category": "Termite Control",
            "serviceType": "WDOR Report"
          }
        ]
      },
      "exclude": []
    },
    "LIMITATION OF LIABILITY": {
      "include": {
        "23": [
          {
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "PAYMENTS": {
      "include": {
        "27": [
          {
            "isBuilder": "False",
            "category": "Termite Control"
          },
          {
            "isBuilder": "True",
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "REINSPECTION": {
      "include": {
        "28": [
          {
            "isBuilder": "False",
            "category": "Termite Control"
          }
        ],
        "29": [
          {
            "isBuilder": "True",
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "RENEWABLE SUBTERRANEAN TERMITE RETREATMENT GUARANTEE": {
      "include": {
        "30": [
          {
            "isBuilder": "True",
            "category": "Termite Control",
            "serviceType": "Termite Bait Station 1"
          },
          {
            "isBuilder": "True",
            "category": "Termite Control",
            "serviceType": "Termite Bait Station Formosan 1"
          }
        ],
        "31": [
          {
            "isBuilder": "False",
            "category": "Termite Control"
          },
          {
            "isBuilder": "True",
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "SERVICE EXCLUSION, WAIVER, AND RELEASE": {
      "include": {
        "32": [
          {
            "category": "Termite Control",
            "serviceType": "Termite Inspection - Termite Account"
          },
          {
            "category": "Termite Control",
            "serviceType": "WDOR Report"
          }
        ],
        "33": [
          {
            "category": "General Pest"
          }
        ]
      },
      "exclude": []
    },
    "SERVICE TO BE PROVIDED": {
      "include": {
        "34": [
          {
            "category": "General Pest"
          }
        ]
      },
      "exclude": [
        {}
      ]
    },
    "TERMINATION": {
      "include": {
        "35": [
          {
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "TRANSFER": {
      "include": {
        "37": [
          {
            "category": "Termite Control"
          }
        ]
      },
      "exclude": [
        {
          "category": "Termite Control",
          "serviceType": "Termite Inspection - Termite Account"
        },
        {
          "category": "Termite Control",
          "serviceType": "WDOR Report"
        }
      ]
    },
    "The Georgia Structural Pest Con...": {
      "include": {
        "38": [
          {
            "stateCode": "GA",
            "category": "Termite Control"
          }
        ],
        "39": [
          {
            "stateCode": "GA"
          }
        ]
      },
      "exclude": []
    },
    "ADDENDUM": {
      "include": {
        "40": [
          {}
        ]
      },
      "exclude": []
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