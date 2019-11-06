module DecimalCounter_tb;

wire [3:0] CNT10;
reg clk;
reg rst;

DecimalCounter
 U0 (
  .CNT10(CNT10),
  .clk(clk),
  .rst(rst));

  initial
  begin
    clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
  end

  initial
  begin
    rst = 1'b0;
    #300 rst = 1'b1;
    #200 rst = 1'b0;
  end

endmodule
