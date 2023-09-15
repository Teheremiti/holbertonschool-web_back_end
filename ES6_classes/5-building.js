/* eslint-disable */
export default class Building {
    constructor(sqft) {
        if (this.constructor !== Building && !this.evacuationWarningMessage) {
            throw Error('Class extending Building must override evacuationWarningMessage');
        }
        this._sqft = sqft;
    }

    get sqft() {
        return this._sqft;
    }

    set sqft(newsqft) {
        this._sqft = newsqft;
    }


}