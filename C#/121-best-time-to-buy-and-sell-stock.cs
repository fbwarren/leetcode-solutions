public int MaxProfit(int[] prices) {
    int output = 0, buyPrice = prices[0];

    foreach (int price in prices) {
        if (price < buyPrice) {
            buyPrice = price;
        } else {
            output = Math.Max(output, price - buyPrice);
        }
    }

    return output;
}
