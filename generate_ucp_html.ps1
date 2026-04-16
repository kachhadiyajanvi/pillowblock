$rawData = @"
12	UCP201	UC201	30.2	127	36	38	16	95	60	12.7	31	13	18	M10
12.7	UCP201-8	UC201-8	30.2	127	36	38	16	95	60	12.7	31	13	18	M10
15	UCP202	UC202	30.2	127	36	38	16	95	60	12.7	31	13	18	M10
15.87	UCP202-10	UC202-10	30.2	127	36	38	16	95	60	12.7	31	13	18	M10
17	UCP203	UC203	30.2	127	36	38	16	95	60	12.7	31	13	18	M10
19.05	UCP204-12	UC204-12	33.3	127	36	38	16	95	65	12.7	31	13	18	M10
20	UCP204	UC204	33.3	127	36	38	16	95	65	12.7	31	13	18	M10
22.22	UCP205-14	UC205-14	37	140	38	38	15	105	70	14.3	34.1	13	18	M10
23.81	UCP205-15	UC205-15	37	140	38	38	15	105	70	14.3	34.1	13	18	M10
25	UCP205	UC205	37	140	38	38	15	105	70	14.3	34.1	13	18	M10
25.4	UCP205-16	UC205-16	37	140	38	38	15	105	70	14.3	34.1	13	18	M10
28.57	UCP206-18	UC206-18	42.9	163	48	47	17	121	82	15.9	38.1	17	21	M14
30	UCP206	UC206	42.9	163	48	47	17	121	82	15.9	38.1	17	21	M14
30.16	UCP206-19	UC206-19	42.9	163	48	47	17	121	82	15.9	38.1	17	21	M14
31.75	UCP206-20	UC206-20	42.9	163	48	47	17	121	82	15.9	38.1	17	21	M14
31.75	UCP207-20	UC207-20	47.6	167	47	46	18	127	93	17.5	42.9	17	21	M14
33.33	UCP207-21	UC207-21	47.6	167	47	46	18	127	93	17.5	42.9	17	21	M14
34.92	UCP207-22	UC207-22	47.6	167	47	46	18	127	93	17.5	42.9	17	21	M14
35	UCP207	UC207	47.6	167	47	46	18	127	93	17.5	42.9	17	21	M14
36.51	UCP207-23	UC207-23	47.6	167	47	46	18	127	93	17.5	42.9	17	21	M14
38.1	UCP208-24	UC208-24	49.2	179	53	54	18	137	98	19	49.2	17	21	M14
39.69	UCP208-25	UC208-25	49.2	179	53	54	18	137	98	19	49.2	17	21	M14
40	UCP208	UC208	49.2	179	53	54	18	137	98	19	49.2	17	21	M14
41.27	UCP209-26	UC209-26	54	189	55	53	21	146	105	19	49.2	17	21	M14
42.86	UCP209-27	UC209-27	54	189	55	53	21	146	105	19	49.2	17	21	M14
44.45	UCP209-28	UC209-28	54	189	55	53	21	146	105	19	49.2	17	21	M14
45	UCP209	UC209	54	189	55	53	21	146	105	19	49.2	17	21	M14
47.62	UCP210-30	UC210-30	57.2	206	60	60	21	159	113	19	51.6	20	22	M16
49.21	UCP210-31	UC210-31	57.2	206	60	60	21	159	113	19	51.6	20	22	M16
50	UCP210	UC210	57.2	206	60	60	21	159	113	19	51.6	20	22	M16
50.8	UCP210-32	UC210-32	57.2	206	60	60	21	159	113	19	51.6	20	22	M16
50.8	UCP211-32	UC211-32	63.5	218	65	60	23	171	124	22.2	55.6	20	25	M16
53.97	UCP211-34	UC211-34	63.5	218	65	60	23	171	124	22.2	55.6	20	25	M16
55	UCP211	UC211	63.5	218	65	60	23	171	124	22.2	55.6	20	25	M16
55.56	UCP211-35	UC211-35	63.5	218	65	60	23	171	124	22.2	55.6	20	25	M16
57.15	UCP212-36	UC212-36	69.8	238	73	70	26	184	136	25.4	65.1	20	25	M16
60	UCP212	UC212	69.8	238	73	70	26	184	136	25.4	65.1	20	25	M16
60.32	UCP212-38	UC212-38	69.8	238	73	70	26	184	136	25.4	65.1	20	25	M16
61.91	UCP212-39	UC212-39	69.8	238	73	70	26	184	136	25.4	65.1	20	25	M16
63.5	UCP213-40	UC213-40	76.2	263	78	70	27	203	149	25.4	65.1	25	30	M20
65	UCP213	UC213	76.2	263	78	70	27	203	149	25.4	65.1	25	30	M20
69.85	UCP214-44	UC214-44	79.4	266	75	72	27	210	157	30.2	74.6	25	30	M20
70	UCP214	UC214	79.4	266	75	72	27	210	157	30.2	74.6	25	30	M20
74.61	UCP215-47	UC215-47	82	274	78	74	28	217	162	33.3	77.8	25	30	M20
75	UCP215	UC215	82	274	78	74	28	217	162	33.3	77.8	25	30	M20
76.2	UCP215-48	UC215-48	82	274	78	74	28	217	162	33.3	77.8	25	30	M20
79.37	UCP216-50	UC216-50	89	292	83	78	30	232	174	33.3	82.6	25	31	M20
80	UCP216	UC216	89	292	83	78	30	232	174	33.3	82.6	25	31	M20
82.55	UCP217-52	UC217-52	95	312	87	83	34	247	186	34.1	85.7	25	32	M20
85	UCP217	UC217	95	312	87	83	34	247	186	34.1	85.7	25	32	M20
88.9	UCP218-56	UC218-56	101.6	327	94	88	33	262	198	39.7	96	27	40	M22
90	UCP218	UC218	101.6	327	94	88	33	262	198	39.7	96	27	40	M22
"@

$lines = $rawData.Trim() -split "`n"
$htmlContent = ""

foreach ($line in $lines) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    $cols = $line.Trim() -split "`t"
    if ($cols.Length -lt 15) { continue }
    
    $shaft = $cols[0]
    $ucp = $cols[1]
    $uc = $cols[2]
    $H = $cols[3]
    $L = $cols[4]
    $L1 = $cols[5]
    $A = $cols[6]
    $H1 = $cols[7]
    $J = $cols[8]
    $H2 = $cols[9]
    $S = $cols[10]
    $B = $cols[11]
    $N = $cols[12]
    $N1 = $cols[13]
    $Bolt = $cols[14]

    $htmlContent += @"
                    <div class="spec-tile" data-designation="$ucp" data-shaft="$shaft">
                        <div class="tile-header">
                            <div class="tile-designation">$ucp</div>
                            <div class="tile-category">Pillow Block</div>
                        </div>
                        <div class="tile-main-spec">
                            <div class="stat-lbl">Shaft Diameter</div>
                            <div class="shaft-value-wrap">
                                <span class="shaft-val">$shaft</span>
                                <span class="shaft-unit">mm</span>
                            </div>
                        </div>
                        <div class="card-table-wrap">
                            <table class="card-table">
                                <tr><td class="td-label">H</td><td class="td-value">$H</td></tr>
                                <tr><td class="td-label">L</td><td class="td-value">$L</td></tr>
                                <tr><td class="td-label">L1</td><td class="td-value">$L1</td></tr>
                                <tr><td class="td-label">A</td><td class="td-value">$A</td></tr>
                                <tr><td class="td-label">H1</td><td class="td-value">$H1</td></tr>
                                <tr><td class="td-label">Pitch (J)</td><td class="td-value">$J</td></tr>
                                <tr><td class="td-label">H2</td><td class="td-value">$H2</td></tr>
                                <tr><td class="td-label">S</td><td class="td-value">$S</td></tr>
                                <tr><td class="td-label">B</td><td class="td-value">$B</td></tr>
                                <tr><td class="td-label">N</td><td class="td-value">$N</td></tr>
                                <tr><td class="td-label">N1</td><td class="td-value">$N1</td></tr>
                            </table>
                        </div>
                        <div class="tile-footer-v2">
                            <div class="tile-bearing" style="font-size:10px; color:rgba(255,255,255,0.4);">Bearing: $uc</div>
                            <div class="tile-bolt" style="font-size:11px; color:var(--primary); font-weight:800; display:flex; align-items:center; gap:5px;"><i data-lucide="settings" style="width:12px; height:12px;"></i> $Bolt</div>
                        </div>
                    </div>
"@
}

$path = "e:\PILLOW BLOCK WEB\product-ucp.html"
$content = Get-Content $path -Raw

# Replace the previous Technical Table area with the Grid of Card-Tables
$pattern = '(?s)<div class="mobile-scroll-hint">.*?</div>\s+<div id="resultsGrid".*?</table>\s+</div>'
$resultsSkeleton = @"
            <div id="resultsGrid" class="tech-results-grid">
$htmlContent
            </div>
"@

if ($content -match $pattern) {
    $content = $content -replace $pattern, $resultsSkeleton
} else {
    # Fallback pattern if previous replacement was slightly different
    $patternFallback = '(?s)<div id="resultsGrid".*?</div>'
    $content = $content -replace $patternFallback, $resultsSkeleton
}

Set-Content -Path $path -Value $content
Write-Output "Successfully updated 52 records into individual Model Technical Tables."
