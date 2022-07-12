pip3 install ethereum-etl
 ethereumetl export_blocks_and_transactions --start-block 0 --end-block 50 \
--blocks-output blocks.csv --transactions-output transactions.csv \
--provider-uri "https://mainnet.infura.io/v3/e95417e91b974e3d81dfc2bfe40aa2c6"
