function monthFormatter() {
    return this.$refs.calendar.getFormatter({
        timeZone: 'UTC',
        month: 'long',
    });
};


function nth(d) {
    return d > 3 && d < 21 ?
        'th' : ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th'][d % 10]
}


export { monthFormatter, nth }