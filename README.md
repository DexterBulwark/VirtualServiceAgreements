# Virtual Service Agreement

This repository contains examples of the expected JSON to receive for service agreements and the HTML that it should be converted to. It also containes examples of how the fine print should be given when requested through an API.

## Rules

### Optional Fields
The majority of fields must be required in the json. The only fields that are not required are:

**ALL**
- `billingInfo` (default to customer info if not provided)
- `savedOn` (this should be filled on our end when the json is recieved)

**GENERAL PEST**
- `services->recurring` (would not be needed for One Time Treatments)

### Service Lists
All `initial services` and `recurring services` are list and can have any number of items. They will always need to follow the following format:




**Initial Service** *(Termite Protection, Initial Warranty Extention)*
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

### Signature

The signature should be recieved as a **base64** encoded image which will be converted on our end and placed into the signature section. 

The image should be a **3000x500** image (JPG, JPEG, PNG, PDF). The dementions should be maintained for consistency. 

### Times

All times should be in UTC time. The one exception being the `intialServiceDate` and `intialServiceTime`. These fields should be expected as a string and look like this:

```json
"initialServiceDate": "Jan 02, 2024",
"initialServiceTime": "1:00PM - 4:00PM",
```


## API Request

### Accept Service Agreements ***(do this first)***

Please build an API that is able to take in the raw JSON, plug in the informaiton to the corresponding HTML template, and save the filled out HTML as a uneditable PDF.

<details>
<summary>Examples</summary>

**General Pest**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/examples/general_pest.json)

- [HTML Code *(empty)*](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/templates/generalPest.html)

- [HTML Code *(filled)*](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/generalPest.html)

- [PDF](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/pdfExamples/generalPest.pdf)

**Termite Control**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/examples/termite_control.json)

- [HTML Code *(empty)*](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/templates/termiteControl.html)

- [HTML Code *(filled)*](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/termiteControl.html)

- [PDF](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/pdfExamples/termiteControl.pdf)

**Termite Warranty**

- [JSON](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/json/examples/termite_warranty.json)

- [HTML Code _(empty)_](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/templates/termiteWarranty.html)

- [HTML Code _(filled)_](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/termiteWarranty.html)

- [PDF](https://github.com/DexterBulwark/VirtualServiceAgreements/blob/main/receiveAgreements/html/examples/pdfExamples/termiteWarranty.pdf)

</details>

### Provide Fine Print ***(do not do this yet)***

Create an API that will accept an office id and return all of the fine print for that office among other information. 

<details>
<summary>Examples</summary>

Empty JSON
``` json
{
    "officeId": 0,
    "license": "",
    "officeName": "",
    "streetAddress": "",
    "city": "",
    "state": "",
    "zip": "",
    "phoneNumber": "",
    "finePrints":
    {
        "nonBuilderSalesSubType":
        [
            {
                "title": "",
                "content": ""
            }
        ],
        "builderSalesSubType":
        [
            {
                "title": "",
                "content": ""
            }
        ]
    }
}

```

<details>
<summary>Filled JSON</summary>

``` json
{
    "officeId": 1,
    "license": "LIC #566944; Licensed and regulated by: Texas Department of Agriculture, P.O. Box 12847, Austin, TX 78711-2847, Phone (866) 918-4481, Fax (888) 232-2567",
    "officeName": "Austin",
    "streetAddress": "209 E Ben White Blvd 116",
    "city": "Austin",
    "state": "TX",
    "zip": "78704",
    "phoneNumber": "(512) 291-1200",
    "finePrints": 
    {
        "nonBuilderSalesSubType": 
        [
            {
                "Pest Control - Houston, San Antonio, Austin & Corpus Christi": "BECAUSE MOST INFESTATIONS START OUTSIDE, BULWARK'S SYSTEM IS DESIGNED TO MAINTAIN A STRONG EXTERIOR BARRIER WHICH IS REINFORCED ON A REGULAR BASIS. SHOULD INSIDE SERVICE BE REQUIRED, PLEASE FEEL FREE TO CONTACT US FOR AN INSIDE VISIT AT NO EXTRA CHARGE. IF SERVICE IS CANCELED PRIOR TO THE LENGTH OF AGREEMENT, THE CUSTOMER AGREES TO PAY ANY DISCOUNTS RECEIVED ON THE INITIAL SERVICE. \r\n\r\nBULWARK PROPERTY: Any bait stations, equipment or devices placed or installed at the Customer's property are not owned by the Customer and may be removed by BULWARK at its discretion, at any time, for any reason, including, but not limited to replacement with an alternative treatment method, as a practice of Integrated Pest Management, or upon the termination of this Agreement.\r\n\r\nConsumer Information Sheet: bulwarkpestcontrol.com/txconsumerinfo\r\n\r\nSERVICE TO BE PROVIDED: After the initial length of agreement, this agreement is automatically renewable on a month to month basis and may be cancelled anytime after the length of agreement by either party giving 30 days written notice.\r\n\r\nAfter the initial length of agreement, this agreement is automatically renewable on a month to month basis and may be cancelled anytime after the length of agreement by either party giving 30 days written notice.\r\n\r\nLATE PAYMENT: If the customer fails, for any reason to make a monthly payment within 30 days from the due date, Bulwark, at its option may discontinue the service and start collection proceedings. Upon failure to make such payments, the customer agrees to pay all cost of collecting, including a reasonable attorney's fee.\r\n\r\nSERVICE EXCLUSION, WAIVER AND RELEASE: I understand that this agreement does not include the control or prevention of wood infesting organisms such as termites, powder post beetles, wood borers, wood wasps, or wood decay fungus. I understand that this agreement does not include the control or prevention of bedbugs. I expressly waive and release Bulwark from liability for any claim for personal injury or damages to the structure or its content caused by wood infesting organisms, fire ants, pharaoh ants, spiders, ticks, wasps, bees or other pests listed in this agreement. I also waive any claims in any lawsuit, arbitration or legal proceeding against Bulwark for (a) loss of use or diminution of value, (b) economic, compensatory, incidental, or consequential damages of any kind, or (c) exemplary or punitive damages.\r\n\r\nARBITRATION: Any dispute arising out of or relating to this agreement or the services performed under this agreement or tort based claims for personal or bodily injury or damage to real or personal property shall be finally resolved by arbitration administered under the Commercial Arbitration rules of the American Arbitration Association. This agreement involves interstate commerce; furthermore, the parties expressly agree that their mutual rights and obligations under the conduct of any arbitration proceeding shall be controlled by the Federal Arbitration Act. The award of the arbitrator shall be final, binding, non-appealable and may be entered and enforced in any court having jurisdiction in accordance with the Federal Arbitration Act. The arbitrator shall not have the power or authority to award exemplary, treble, liquidated or any type of punitive damages.\r\n\r\nCHEMICAL SENSITIVITY: Virtually all pesticides have some odor which may be present for a short while after application. If you or any member of your household has a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have your home serviced for pest control until you have consulted your family physician.",
                "OTT Pest Control - Houston, San Antonio, Austin & Corpus Christi": "BECAUSE MOST INFESTATIONS START OUTSIDE, BULWARK'S SYSTEM IS DESIGNED TO MAINTAIN A STRONG EXTERIOR BARRIER WHICH IS REINFORCED ON A REGULAR BASIS. SHOULD INSIDE SERVICE BE REQUIRED, PLEASE FEEL FREE TO CONTACT US FOR AN INSIDE VISIT AT NO EXTRA CHARGE. IF SERVICE IS CANCELED PRIOR TO THE LENGTH OF AGREEMENT, THE CUSTOMER AGREES TO PAY ANY DISCOUNTS \r\nRECEIVED ON THE INITIAL SERVICE. \r\n\r\nBULWARK PROPERTY: Any bait stations, equipment or devices placed or installed at the Customer's property are not owned by the Customer and may be removed by BULWARK at its discretion, at any time, for any reason, including, but not limited to replacement with an alternative treatment method, as a practice of Integrated Pest Management, or upon the termination of this Agreement.\r\n\r\nConsumer Information Sheet: bulwarkpestcontrol.com/txconsumerinfo\r\n\r\nLATE PAYMENT: If the customer fails, for any reason to make a monthly payment within 30 days from the due date, Bulwark, at its option may discontinue the service and start collection proceedings. Upon failure to make such payments, the customer agrees to pay all cost of collecting, including a reasonable attorney's fee.\r\n\r\nSERVICE EXCLUSION, WAIVER AND RELEASE: I understand that this agreement does not include the control or prevention of wood infesting organisms such as termites, powder post beetles, wood borers, wood wasps, or wood decay fungus. I understand that this agreement does not include the control or prevention of bedbugs. I expressly waive and release Bulwark from liability for any claim for personal injury or damages to the structure or its content caused by wood infesting organisms, fire ants, pharaoh ants, spiders, ticks, wasps, bees or other pests listed in this agreement. I also waive any claims in any lawsuit, arbitration or legal proceeding against Bulwark for (a) loss of use or diminution of value, (b) economic, compensatory, incidental, or consequential damages of any kind, or (c) exemplary or punitive damages.\r\n\r\nARBITRATION: Any dispute arising out of or relating to this agreement or the services performed under this agreement or tort based claims for personal or bodily injury or damage to real or personal property shall be finally resolved by arbitration administered under the Commercial Arbitration rules of the American Arbitration Association. This agreement involves interstate commerce; furthermore, the parties expressly agree that their mutual rights and obligations under the conduct of any arbitration proceeding shall be controlled by the Federal Arbitration Act. The award of the arbitrator shall be final, binding, non-appealable and may be entered and enforced in any court having jurisdiction in accordance with the Federal Arbitration Act. The arbitrator shall not have the power or authority to award exemplary, treble, liquidated or any type of punitive damages.\r\n\r\nCHEMICAL SENSITIVITY: Virtually all pesticides have some odor which may be present for a short while after application. If you or any member of your household has a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have your home serviced for pest control until you have consulted your family physician.",
                "WDOR or TTI": "LATE PAYMENT: If the customer fails, for any reason, to make a payment within 30 days from the due date, Bulwark, at its option, may start collection proceedings. Upon failure to make such payments, the customer agrees to pay all costs of collecting, including a reasonable attorney's fee.\r\n\r\nSERVICE EXCLUSION, WAIVER, AND RELEASE: I understand that this agreement does not include the control or prevention of wood infesting organisms such as termites, powder post beetles, wood borers, carpenter ants, carpenter bees, wood wasps, or wood decay fungus. I expressly waive and release Bulwark from liability for any claim for personal injury or damages to the structure or its content caused by wood infesting organisms. I also waive any claims in any lawsuit, arbitration, or legal proceeding against Bulwark for (a) loss of use or diminution of value, (b) economic, compensatory, incidental, or consequential damages of any kind, or (c) exemplary or punitive damages.\r\n\r\nARBITRATION: Any dispute arising out of or relating to this agreement or the services performed under this agreement or tort based claims for personal or bodily injury or damage to real or personal property shall be finally resolved by arbitration administered under the Commercial Arbitration rules of the American Arbitration Association. This agreement involves interstate commerce; furthermore, the parties expressly agree that their mutual rights and obligations under the conduct of any arbitration proceeding shall be controlled by the Federal Arbitration Act. The arbitrator shall not have the power or authority to award exemplary, treble, liquidated, or any type of punitive damages.",
                "Trelona ATBS Baiting Protection Plan - Austin, Corpus Christi, Houston, San Antonio": "BULWARK is hereby authorized to place bait stations in and around Customer's building described in the attached Subterranean Termite Post-Construction Treatment Disclosure for prevention and control of Subterranean Termites.\r\n\r\nIMPORTANT: Customer understands that Bulwark will not be responsible for repairs or replacement of damaged material to the structure or its contents caused by Subterranean Termites or other wood destroying organisms. If during the effective period of this agreement, BULWARK, for whatever reason, changes the type of bait being used or ceases to offer a bait program in this area, if available, an appropriate alternative treatment method will be determined by and performed by BULWARK. Any bait stations, equipment or devices placed or installed at the Customer's property are not owned by the Customer and may be removed by BULWARK at its discretion, at any time, for any reason, including, but not limited to; replacement with an alternative treatment method, as a practice of Integrated Pest Management, or upon the termination of this Agreement, or, if Bulwark ceases to offer a bait program in this area. Service includes Bait System installation and Warranty as specified by BULWARK. BULWARK'S services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any liability for any claim for personal injury resulting from the services performed, under this contract, or damages to the structure or its contents whether preexisting or after the services are performed, caused by an infestation of Formosan Termites, Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. Customer shall receive the following Guarantee after the initial service is performed.\r\n\r\nRENEWABLE SUBTERRANEAN TERMITE RETREATMENT GUARANTEE: So long as Customer complies with the Customer obligations below, and provided that all payments of the applicable Retreatment Guarantee Fees are current, if Bulwark is notified that an infestation of Subterranean Termites has been found, Bulwark will, on inspection, either retreat the structure for Subterranean Termites at no additional cost to the Customer or Customer may cancel this agreement. CUSTOMER EXPRESSLY RELEASES BULWARK FROM ANY AND ALL CLAIMS FOR PERSONAL INJURY, PROPERTY DAMAGE, AND FOR SUBTERRANEAN TERMITE DAMAGE OR REPAIR.\r\n\r\nCUSTOMER'S OBLIGATIONS TO MAINTAIN RETREATMENT GUARANTEE: Customer shall make the premises and structure(s) on premises available to BULWARK for inspections and treatments, as BULWARK deems necessary, which may include the removal of floor coverings, wall coverings and fixtures. Failure to honor the requirements to maintain the structure or to allow BULWARK access for inspections or treatments as appropriate will void the Retreatment Guarantee.\r\n\r\nPAYMENTS: The estimated price and proposed treatment technique verbally provided are subject to change after a physical inspection of the property is performed by a Bulwark Inspector. This may include extra charges for costlier treatment techniques or additional control measures needed. The initial payment covers the installation of the bait stations and/or the liquid treatment, and is due at the time the initial service is performed. After the initial installation the Warranty Fee will be assessed on a monthly basis. By payment of the Warranty Fee, this Agreement may be renewed monthly. As long as Customer keeps the BULWARK Warranty Fee current, BULWARK will monitor Customer's structure and maintain the Guarantee under this Agreement. \r\n\r\nREINSPECTION: BULWARK shall reinspect the treated structures on Customer's premises as deemed necessary by BULWARK or as requested by Customer.\r\n\r\nARBITRATION: IN THE EVENT OF ANY DISPUTE ARISING OUT OF OR RELATING TO THE SERVICES PERFORMED UNDER THIS AGREEMENT OR TORT CLAIMS FOR PERSONAL OR BODILY INJURY OR DAMAGE TO REAL OR PERSONAL PROPERTY, THE PARTIES FIRST AGREE TO PARTICIPATE IN AT LEAST FOUR (4) HOURS OF MEDIATION IN ACCORDANCE WITH THE COMMERCIAL MEDIATION RULES OF THE AMERICAN ARBITRATION ASSOCIATION BEFORE HAVING RECOURSE TO ARBITRATION. IF THE MEDIATION PROCEDURE PROVIDED FOR HEREIN DOES NOT RESOLVE SUCH DISPUTE, THE PARTIES AGREE THAT ALL CONTROVERSIES OR CLAIMS ARISING OUT OF OR RELATING TO THIS AGREEMENT, OR THE BREACH THEREOF, SHALL BE SETTLED BY ARBITRATION ADMINISTERED BY THE AMERICAN ARBITRATION ASSOCIATION UNDER ITS COMMERCIAL ARBITRATION RULES, AND JUDGMENT ON THE AWARD RENDERED BY THE ARBITRATOR(S) MAY BE ENTERED IN ANY COURT HAVING JURISDICTION THEREOF. THE ARBITRATOR SHALL GIVE EFFECT TO ANY AND ALL WAIVERS, RELEASED, DISCLAIMERS, LIMITATIONS AND OTHER TERMS AND CONDITIONS OF THIS AGREEMENT, AS WELL AS LEGAL DEFENSES RAISED BY EITHER PARTY.\r\n\r\nLIMITATION OF LIABILITY: Customer waives any claims for personal injury and/or property damages related to the Services BULWARK performs under this Agreement. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises while treating their structures, including any damage to shrubs, trees, or plants. The Services performed by BULWARK may include drilling through concrete or the structure itself. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises as a result of drilling, including but not limited to damage caused to plumbing or electrical pipes, wires, or conduits. To avoid potential damage, customer is advised to use a utility locating service to identify the location of the utility lines in or near the structures prior to BULWARK‘S Services. When performing the Services, it may be necessary for Customer to remove floor coverings, floors, excavate crawl spaces and provide access to walls, ceilings, or floors. Customer shall be responsible for the cost of dismantling and reconstruction of any item required in order to provide adequate access for providing Services. Customer acknowledges that modifications or alterations to the structure during this agreement may void this Retreatment Guarantee. Customer is advised to notify BULWARK in advance to determine whether such modifications or alterations will void the Retreatment Guarantee or if additional Services will be required at an additional cost to the Customer in order to validate the Retreatment Guarantee. Customer expressly waives and releases BULWARK from and against any claims for (a) loss of use or diminution of property value, (b) economic, compensatory, incidental, or consequential damages and/or (c) exemplary or punitive damages. Customer further agrees that under no circumstances shall BULWARK be liable for any amount greater than the amount paid by Customer to BULWARK for the Services performed.\r\n\r\nTRANSFER: This Agreement is transferable to a new property owner upon written notice to BULWARK and new owner's assumption of the Retreatment Guarantee fee. \r\n\r\nCHEMICAL SENSITIVITY: At times additional termiticides may be used to control termites. These additional termiticides may have some odor which may be present for a short time after application. If you or any member of your household believes you have a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have any Services performed at your premises until you have consulted with your family physician. At your request, Bulwark will provide information about the chemicals to be used in treating the premises.\r\n\r\nAGREEMENT: This Agreement shall be the entire Agreement between Customer and BULWARK for the Services. The terms and the guarantee stated in this Agreement may not be amended or altered unless a written change is approved and signed by The Director of Operations of BULWARK EXTERMINATING, LLC.\r\n\r\nFORCE MAJEURE (Circumstances beyond BULWARK'S control): BULWARK'S obligations under this Agreement shall be suspended or canceled if Bulwark is unable to perform its responsibilities due to a substantial change of circumstances, including, but not limited to acts of war, strikes, pandemics, unavailability of termiticides, or other supplies from ordinary sources, or if acts of God or natural occurrences, such as earthquakes, storms, fires and floods substantially alters or destroys the effectiveness of Bulwark's treatment.\r\n\r\nTERMINATION: BULWARK may terminate this Agreement, including the Guarantee and any renewal rights, contained herein, if Customer does not meet its payment or other Customer obligations, or in the event of a change in state, federal, or local law that substantially affects BULWARK'S obligations under this Agreement. Customer may cancel this agreement at any time prior to midnight of the third business day after the date of this transaction. After midnight of the third business day after the date of this transaction, either party may cancel this agreement giving 30 days written notice to the other party. Any amounts due and unpaid under this Agreement are subject to late fees of ten percent (10%) of the unpaid amount and interest at the rate of ten percent (10%) per annum, as well as attorney fees and collection costs whether or not suit is brought.\r\n\r\nConsumer Information Sheet: bulwarkpestcontrol.com/txconsumerinfo"
            },
        ]
        "builderSalesSubType": 
        [
            {
                "Termite Warranty - San Antonio & Austin": "IMPORTANT: Customer understands that BULWARK will not be responsible for repairs or replacement of damaged material to any structure situated on Customer's premises or their contents caused by Subterranean Termites or other wood destroying organisms. The term “Service” or “Services” under this Agreement means the Bulwark Retreatment Guarantee set forth below. BULWARK'S Retreatment Guarantee and Services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any and all claims of liability for personal injury and/or property damage resulting from the Services performed, by Bulwark including damages to Customer's home, other structures, or their contents, whether preexisting or after the Services are performed, caused by an infestation of, or damage resulting from Subterranean Termites (including Formosan Termites), Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. The following Retreatment Guarantee shall be effective upon payment of the above Retreatment Guarantee Fees and/or payment of $1.00 to initiate this AGREEMENT.\r\n\r\nRENEWABLE SUBTERRANEAN TERMITE RETREATMENT GUARANTEE: So long as Customer complies with the Customer obligations below, and provided that all payments of the applicable Retreatment Guarantee Fees are current, if Bulwark is notified that an infestation of Subterranean Termites has been found, Bulwark will, on inspection, either retreat the structure for Subterranean Termites, at no additional cost to the Customer, or Customer may cancel this agreement. CUSTOMER EXPRESSLY RELEASES BULWARK FROM ANY AND ALL CLAIMS FOR PERSONAL INJURY, PROPERTY DAMAGE, AND FOR SUBTERRANEAN TERMITE DAMAGE OR REPAIR.\r\n\r\nCUSTOMER'S OBLIGATIONS TO MAINTAIN RETREATMENT GUARANTEE: Customer shall make the premises and structure(s) on premises available to BULWARK for inspections and treatments, as BULWARK deems necessary, which may include the removal of floor coverings, wall coverings and fixtures. Failure to honor the requirements to maintain the structure or to allow BULWARK access for inspections or treatments as appropriate will void the Retreatment Guarantee.\r\n\r\nPAYMENTS: Your payment of the Retreatment Guarantee Fee extends subterranean termite protection for work performed by BULWARK during the construction of your home. At the end of Bulwark's Guarantee Expiration Date this agreement automatically renews on a month-to-month basis. So long as the Retreatment Guarantee Fee is paid when due, BULWARK will honor the Retreatment Guarantee.\r\n\r\nREINSPECTION: BULWARK shall reinspect the treated structures on Customer's premises as deemed necessary by BULWARK or as requested by Customer. The frequency of these inspections shall be in accordance with the Trelona ATBS product label.\r\n\r\nARBITRATION: IN THE EVENT OF ANY DISPUTE ARISING OUT OF OR RELATING TO THE SERVICES PERFORMED UNDER THIS AGREEMENT OR TORT CLAIMS FOR PERSONAL OR BODILY INJURY OR DAMAGE TO REAL OR PERSONAL PROPERTY, THE PARTIES FIRST AGREE TO PARTICIPATE IN AT LEAST FOUR (4) HOURS OF MEDIATION IN ACCORDANCE WITH THE COMMERCIAL MEDIATION RULES OF THE AMERICAN ARBITRATION ASSOCIATION BEFORE HAVING RECOURSE TO ARBITRATION. IF THE MEDIATION PROCEDURE PROVIDED FOR HEREIN DOES NOT RESOLVE SUCH DISPUTE, THE PARTIES AGREE THAT ALL CONTROVERSIES OR CLAIMS ARISING OUT OF OR RELATING TO THIS AGREEMENT, OR THE BREACH THEREOF, SHALL BE SETTLED BY ARBITRATION ADMINISTERED BY THE AMERICAN ARBITRATION ASSOCIATION UNDER ITS COMMERCIAL ARBITRATION RULES, AND JUDGMENT ON THE AWARD RENDERED BY THE ARBITRATOR(S) MAY BE ENTERED IN ANY COURT HAVING JURISDICTION THEREOF. THE ARBITRATOR SHALL GIVE EFFECT TO ANY AND ALL WAIVERS, RELEASED, DISCLAIMERS, LIMITATIONS AND OTHER TERMS AND CONDITIONS OF THIS AGREEMENT, AS WELL AS LEGAL DEFENSES RAISED BY EITHER PARTY.\r\n\r\nLIMITATION OF LIABILITY: Customer waives any claims for personal injury and/or property damages related to the Services BULWARK performs under this Agreement. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises while treating their structures, including any damage to shrubs, trees, or plants. The Services performed by BULWARK may include drilling through concrete or the structure itself. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises as a result of drilling, including but not limited to damage caused to plumbing or electrical pipes, wires, or conduits. To avoid potential damage, customer is advised to use a utility locating service to identify the location of the utility lines in or near the structures prior to BULWARK‘S Services. When performing the Services, it may be necessary for Customer to remove floor coverings, floors, excavate crawl spaces and provide access to walls, ceilings, or floors. Customer shall be responsible for the cost of dismantling and reconstruction of any item required in order to provide adequate access for providing Services. Customer acknowledges that modifications or alterations to the structure during this agreement may void this Retreatment Guarantee. Customer is advised to notify BULWARK in advance to determine whether such modifications or alterations will void the Retreatment Guarantee or if additional Services will be required at an additional cost to the Customer in order to validate the Retreatment Guarantee. Customer expressly waives and releases BULWARK from and against any claims for (a) loss of use or diminution of property value, (b) economic, compensatory, incidental, or consequential damages and/or (c) exemplary or punitive damages. Customer further agrees that under no circumstances shall BULWARK be liable for any amount greater than the amount paid by Customer to BULWARK for the Services performed.\r\n\r\nTRANSFER: This Agreement is transferable to a new property owner upon written notice to BULWARK and new owner's assumption of the Retreatment Guarantee fee. \r\n\r\nCHEMICAL SENSITIVITY: At times additional termiticides may be used to control termites. These additional termiticides may have some odor which may be present for a short time after application. If you or any member of your household believes you have a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have any Services performed at your premises until you have consulted with your family physician. At your request, Bulwark will provide information about the chemicals to be used in treating the premises.\r\n\r\nAGREEMENT: This Agreement shall be the entire Agreement between Customer and BULWARK for the Services. The terms and the guarantee stated in this Agreement may not be amended or altered unless a written change is approved and signed by The Director of Operations of BULWARK EXTERMINATING, LLC.\r\n\r\nFORCE MAJEURE (Circumstances beyond BULWARK'S control): BULWARK'S obligations under this Agreement shall be suspended or cancelled if Bulwark is unable to perform its responsibilities due to a substantial change of circumstances, including, but not limited to acts of war, strikes, pandemics, unavailability of termiticides, or other supplies from ordinary sources, or if acts of God or natural occurrences, such as earthquakes, storms, fires and floods substantially alters or destroys the effectiveness of Bulwark's treatment.\r\n\r\nTERMINATION: BULWARK may terminate this Agreement, including the Guarantee and any renewal rights, contained herein, if Customer does not meet its payment or other Customer obligations, or in the event of a change in state, federal, or local law that substantially affects BULWARK'S obligations under this Agreement. Customer may cancel this agreement at any time prior to midnight of the third business day after the date of this transaction. After midnight of the third business day after the date of this transaction, either party may cancel this agreement giving 30 days written notice to the other party. Any amounts due and unpaid under this Agreement are subject to late fees of ten percent (10%) of the unpaid amount and interest at the rate of ten percent (10%) per annum, as well as attorney fees and collection costs whether or not suit is brought.\r\n\r\nConsumer Information Sheet: bulwarkpestcontrol.com/txconsumerinfo\r\n",
                "Termite Warranty - Bait Station (Not Houston)": "BULWARK is hereby authorized to install bait stations in and around Customer's premises on the Installation Date Range listed on this AGREEMENT. Prior to Installation, BULWARK will provide Customer a Subterranean Termite Post-Construction Treatment Estimate / Disclosure Document.\r\n\r\nIMPORTANT: Customer understands that BULWARK will not be responsible for repairs or replacement of damaged material to any structure situated on Customer's premises or their contents caused by Subterranean Termites or other wood destroying organisms. The term “Service” or “Services” under this Agreement means the bait station program, and Guarantee set forth below. If during the effective period of this Agreement, BULWARK, for whatever reason, changes the type of bait being used or ceases to offer a bait program in Customer's area, an appropriate alternative treatment method, if available, will be determined by and performed by BULWARK at no additional charge to Customer. The bait stations and all components are owned at all times by BULWARK and may be removed at any time by BULWARK at its discretion, (i) for replacement with an alternative treatment method, (ii) upon the termination of this Agreement; or, (iii) if BULWARK ceases to offer a bait program in this Customer's area. BULWARK'S Services under this Agreement are expressly related to Subterranean Termites. Customer expressly waives and releases BULWARK from any and all claims of liability for personal injury and/or property damage resulting from the Services performed, by Bulwark including damages to Customer's home, other structures, or their contents, whether preexisting or after the Services are performed, caused by an infestation of, or damage resulting from Subterranean Termites (including Formosan Termites), Boring Beetles, Wood Decay Fungus or any other Wood Destroying organisms. Customer shall receive the following Retreatment Guarantee after the installation of the bait stations and payment.\r\n\r\nRENEWABLE SUBTERRANEAN TERMITE RETREATMENT GUARANTEE: So long as Customer complies with the Customer obligations below, and provided that all payments including guarantee fees are current, if Bulwark is notified that an infestation of Subterranean Termites has been found, Bulwark will, on inspection, either retreat the structure for Subterranean Termites at no additional cost to the Customer or Customer may cancel this agreement and Bulwark will refund Customer's installation charges. CUSTOMER EXPRESSLY RELEASES BULWARK FROM ANY AND ALL CLAIMS FOR PERSONAL INJURY, PROPERTY DAMAGE, AND FOR SUBTERRANEAN TERMITE DAMAGE OR REPAIR.\r\n\r\nCUSTOMER'S OBLIGATIONS TO MAINTAIN RETREATMENT GUARANTEE: Customer agrees not to remove, tamper with, or cover bait stations. Customer shall make the premises and structure(s) on premises available to BULWARK for inspections and treatments, either liquid or bait as BULWARK deems necessary, which may include the removal of floor coverings, wall coverings and fixtures. Failure to honor the requirements to maintain the structure or to allow BULWARK access for inspections or treatments as appropriate will void the Retreatment Guarantee.\r\n\r\nPAYMENTS: Your payment of the Retreatment Guarantee Fee extends subterranean termite protection for work performed by BULWARK during the construction of your home. At the end of Bulwark's Guarantee Expiration Date this agreement automatically renews on a month-to-month basis. So long as the Retreatment Guarantee Fee is paid when due, BULWARK will honor the Retreatment Guarantee.\r\n\r\nREINSPECTION: BULWARK shall reinspect the treated structures on Customer's premises as deemed necessary by BULWARK or as requested by Customer. The frequency of these inspections shall be in accordance with the Trelona ATBS product label.\r\n\r\nARBITRATION: IN THE EVENT OF ANY DISPUTE ARISING OUT OF OR RELATING TO THE SERVICES PERFORMED UNDER THIS AGREEMENT OR TORT CLAIMS FOR PERSONAL OR BODILY INJURY OR DAMAGE TO REAL OR PERSONAL PROPERTY, THE PARTIES FIRST AGREE TO PARTICIPATE IN AT LEAST FOUR (4) HOURS OF MEDIATION IN ACCORDANCE WITH THE COMMERCIAL MEDIATION RULES OF THE AMERICAN ARBITRATION ASSOCIATION BEFORE HAVING RECOURSE TO ARBITRATION. IF THE MEDIATION PROCEDURE PROVIDED FOR HEREIN DOES NOT RESOLVE SUCH DISPUTE, THE PARTIES AGREE THAT ALL CONTROVERSIES OR CLAIMS ARISING OUT OF OR RELATING TO THIS AGREEMENT, OR THE BREACH THEREOF, SHALL BE SETTLED BY ARBITRATION ADMINISTERED BY THE AMERICAN ARBITRATION ASSOCIATION UNDER ITS COMMERCIAL ARBITRATION RULES, AND JUDGMENT ON THE AWARD RENDERED BY THE ARBITRATOR(S) MAY BE ENTERED IN ANY COURT HAVING JURISDICTION THEREOF. THE ARBITRATOR SHALL GIVE EFFECT TO ANY AND ALL WAIVERS, RELEASED, DISCLAIMERS, LIMITATIONS AND OTHER TERMS AND CONDITIONS OF THIS AGREEMENT, AS WELL AS LEGAL DEFENSES RAISED BY EITHER PARTY.\r\n\r\nLIMITATION OF LIABILITY: Customer waives any claims for personal injury and/or property damages related to the Services BULWARK performs under this Agreement. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises while treating their structures, including any damage to shrubs, trees, or plants. The Services performed by BULWARK may include drilling into soil, through concrete or the structure itself. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises as a result of drilling, including but not limited to damage caused to plumbing or electrical pipes, wires, or conduits. To avoid potential damage, customer is advised to use a utility locating service to identify the location of the utility lines in or near the structures prior to BULWARK‘S Services. When performing the Services, it may be necessary for Customer to remove floor coverings, floors, excavate crawl spaces and provide access to walls, ceilings, or floors. Customer shall be responsible for the cost of dismantling and reconstruction of any item required in order to provide adequate access for providing Services. Customer acknowledges that modifications or alterations to the structure during this agreement may void this Retreatment Guarantee. Customer is advised to notify BULWARK in advance to determine whether such modifications or alterations will void the Retreatment Guarantee or if additional Services will be required at an additional cost to the Customer in order to validate the Retreatment Guarantee. Customer expressly waives and releases BULWARK from and against any claims for (a) loss of use or diminution of property value, (b) economic, compensatory, incidental, or consequential damages and/or (c) exemplary or punitive damages. Customer further agrees that under no circumstances shall BULWARK be liable for any amount greater than the amount paid by Customer to BULWARK for the Services performed.\r\n\r\nTRANSFER: This Agreement is transferable to a new property owner upon written notice to BULWARK and new owner's assumption of the Retreatment Guarantee fee. \r\n\r\nCHEMICAL SENSITIVITY: At times additional termiticides may be used to control termites. These additional termiticides may have some odor which may be present for a short time after application. If you or any member of your household believes you have a sensitivity to chemical odor or chemicals, Bulwark recommends that you not have any Services performed at your premises until you have consulted with your family physician. At your request, Bulwark will provide information about the chemicals to be used in treating the premises.\r\n\r\nAGREEMENT: This Agreement shall be the entire Agreement between Customer and BULWARK for the Services. The terms and the guarantee stated in this Agreement may not be amended or altered unless a written change is approved and signed by The Director of Operations of BULWARK EXTERMINATING, LLC.\r\n\r\nFORCE MAJEURE (Circumstances beyond BULWARK'S control): BULWARK'S obligations under this Agreement shall be suspended or cancelled if Bulwark is unable to perform its responsibilities due to a substantial change of circumstances, including, but not limited to acts of war, strikes, pandemics, unavailability of termiticides, or other supplies from ordinary sources, or if acts of God or natural occurrences, such as earthquakes, storms, fires and floods substantially alters or destroys the effectiveness of Bulwark's treatment.\r\n\r\nTERMINATION: BULWARK may terminate this Agreement, including the Guarantee and any renewal rights, contained herein, if Customer does not meet its payment or other Customer obligations, or in the event of a change in state, federal, or local law that substantially affects BULWARK'S obligations under this Agreement. Customer may cancel this agreement at any time prior to midnight of the third business day after the date of this transaction. After midnight of the third business day after the date of this transaction, either party may cancel this agreement giving 30 days written notice to the other party. Any amounts due and unpaid under this Agreement are subject to late fees of ten percent (10%) of the unpaid amount and interest at the rate of ten percent (10%) per annum, as well as attorney fees and collection costs whether or not suit is brought."
            }
        ]
    }
}

```
</details>


</details>
