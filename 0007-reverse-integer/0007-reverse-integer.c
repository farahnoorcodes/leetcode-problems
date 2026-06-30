int reverse(int x) {
    long sign = (x < 0) ? -1 : 1;
    long lx = (long)x * sign;   // safe: long can hold 2147483648 with no overflow
    
    int r, n;
    long rev = 0;
    while (lx > 0) {
        r = lx % 10;
        n = lx / 10;
        rev = rev * 10 + r;
        lx = n;
    }
    
    rev = sign * rev;
    
    if (rev > 2147483647 || rev < -2147483648) {
        return 0;
    }
    
    return (int)rev;
}