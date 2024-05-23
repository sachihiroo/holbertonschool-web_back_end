export default class Currency {
  constructor(code, name) {
    // Store attributes in underscore-prefixed private variables
    this._code = code;
    this._name = name;
  }

  // Getter for _code
  get code() {
    return this._code;
  }

  // Setter for _code
  set code(value) {
    this._code = value;
  }

  // Getter for _name
  get name() {
    return this._name;
  }

  // Setter for _name
  set name(value) {
    this._name = value;
  }

  // Method to display full currency details
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
