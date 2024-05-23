export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // Getter for _amount
  get amount() {
    return this._amount;
  }

  // Setter for _amount
  set amount(value) {
    this._amount = value;
  }

  // Getter for _currency
  get currency() {
    return this._currency;
  }

  // Setter for _currency
  set currency(value) {
    this._currency = value;
  }

  // Method to display full price
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Static method to convert price
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
