# Virtual Service Agreement

This is the template for a digital service agreement. Using the JSON and HTML templates, we should be able to build a system that allows us to deal with service agreements in house.

## Content

There are 4 notable files:
- **service_agreement_empty.json**
    - Template for json data
- **service_agreement_filled.json**
    - Example of filled json data
- **serviceAgreementEmpty.html**
    - Sample html template with values to be filled. ***{{example}}***
- **serviceAgreementFilled.html**
    - Example of fully filled service agreement

## Rules

### Optional Fields
The majority of fields must be required in the json. The only fields that are not required are:
- `billingInfo` (default to customer info if not provided)
- `recurringServices` (would not be needed for One Time Treatments)
- `savedOn` (this should be filled on our end when the json is recieved)

### Service Lists
`initialServices` and `recurringServices` are list and can have any number of items added. They will always need to follow the following format:

**Initial Service**
```json
"initialServices": [
    {
        "serviceName": "",
        "serviceCost": 0.00
    }
],
```

**Recurring Service**
```json
"recurringServices": [
    {
        "serviceName": "",
        "serviceCost": 0.00,
        "paymentFrequency": ""
    }
],
```

And should appear in the HTML like this:

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

### Signature

The signature should be recieved as a **base64** encoded image which would be converted on our end and placed into the signature section. 

The test ran where using a **3000x500** png image. The file type should not be too important but the dementions should be maintained for consistency. 

### Times

All times should be in UTC time. The one exception being the `intialServiceDate` and `intialServiceTime`. These fields should be expected as a string and look like this:

```json
"initialServiceDate": "Jan 02, 2024",
"initialServiceTime": "1:00PM - 4:00PM",
```