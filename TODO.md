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
- Closet [ForeignKey],[array]
  - array of purchased items
- Cart [ForeignKey],[array]
  - array of items in cart

### User Fuctions

Email Reciept

- Send User name, email, and order to Mailchimp
- Import template from Mailchimp
- Send User Form Mandrill

Shipping Updates

- Send User phone number, order to Twilio
- Twilio sends text with order confirmation and status

Closet

- Query all user items

Location

- retrieve all users by city or zip code

## Cart

- id [Integer]
- User [ForeignKey],[integer]
- items [ForeignKey],[Array]

### Cart Fuctions

Transfer Cart Conents to Order

Add to Cart

- add item.id to cart array

## Order

- id [Integer]
- User [ForeignKey],[integer]
- confirmation [String]
- items [Array]
- status [String]
