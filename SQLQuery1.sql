SELECT WELL_BORE_CODE, --To differentiate different wellbore
COUNT(WELL_BORE_CODE) AS recordCount,
WELL_TYPE + ' ' + FLOW_KIND AS wellType,
MIN(AVG_DOWNHOLE_TEMPERATURE) AS [minDownholeTemp],
MAX(AVG_ANNULUS_PRESS) AS [maxAnnulusPress],
AVG(AVG_DP_TUBING) AS [avgDpTubing],
SUM(BORE_OIL_VOL) AS [totalOilVolume],
SUM(BORE_GAS_VOL) AS [totalGasVolume],
SUM(BORE_WAT_VOL) AS [totalWaterVolume]
FROM dbo.production_data_volve
GROUP BY WELL_BORE_CODE, WELL_TYPE + ' ' + FLOW_KIND
ORDER BY totalOilVolume DESC, totalGasVolume DESC, totalWaterVolume DESC