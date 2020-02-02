# TODO

## User

- id [Integer]
- email (unique) [String]
  - blog updates (Mailchimp, Mandrill)
- phone number [Integer]
  - shipping updates (Twilio)
- address [String]
- city
- zip code
- Orders [ForeignKey],[array]
- Closet [ForeignKey],[array]
  - array of purchased items
- Cart [ForeignKey],[array]
  - array of items in cart

### User Fuctions

Create User

Verify Address

Closet

- Query all user items

Location

- retrieve all users by city or zip code

## Cart

- id [Integer]
- User [ForeignKey],[integer]
  - None if empty
- items [ForeignKey],[Array]

### Cart Fuctions

Create Cart

Add to Cart

- add item.id to cart array

Calculate Cost

- return sum of items in array

Payment (Stripe)

- Create User
- Create charge for Stripe
- Upon completion create Order

Create Order

- Create order from cart contents

## Order

- id [Integer]
- User [ForeignKey],[integer]
- confirmation [String]
- items [Array]
- status [String]
  - statuses: recieved, sent, delivered

### Order Functions

Create Item

- create each item
  Email Reciept

- Send User name, email, and order to Mailchimp
- Import template from Mailchimp
- Send User Form Mandrill

Shipping Updates

- Upon status changes, send User phone number, order to Twilio
- Import status template {recieved, sent, delivered}
- Twilio sends text with order confirmation and status

Add to Closet

- Upon delievered status, add order contents to User closet

## Item

- id [Integer]
- type [String]
  - types: shirt
- cost [Integer]
