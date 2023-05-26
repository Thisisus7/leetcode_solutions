var TimeMap = function() {
    this.hash = {};
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if (!this.hash[key]) this.hash[key] = [];
    this.hash[key].push([value, timestamp]);
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    let res = "";
    values = this.hash[key];
    let l = 0, r = Array.isArray(values) ? values.length - 1 : -1;
    while (l <= r) {
        m = Math.floor((l + r) / 2);
        if (values[m][1] <= timestamp) {
            res = values[m][0];
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    return res;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */