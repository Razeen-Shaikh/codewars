function array_diff(a, b) {
    b.forEach(bnum => {
        a = a.filter(anum => anum != bnum);
    });
    return a;
}