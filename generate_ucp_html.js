const fs = require('fs');

const rawData = `12	UCP201	UC201	30.2	127	36	38	16	95	60	12.7	31	13	18	M10
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
90	UCP218	UC218	101.6	327	94	88	33	262	198	39.7	96	27	40	M22`;

const htmlLines = rawData.trim().split('\n').map(line => {
    const cols = line.split('\t').map(l => l.trim());
    if(cols.length < 15) return '';
    const [shaft, ucp, uc, H, L, L1, A, H1, J, H2, S, B, N, N1, Bolt] = cols;
    
    return \`
                    <div class="spec-tile" data-designation="\${ucp}" data-shaft="\${shaft}">
                        <div class="tile-header"><div class="tile-designation">\${ucp}</div><div class="tile-category">Pillow Block</div></div>
                        <div class="tile-main-spec"><div class="stat-lbl">Shaft Diameter</div><div class="shaft-value-wrap"><span class="shaft-val">\${shaft}</span><span class="shaft-unit">mm</span></div></div>
                        <div class="tile-stats" style="grid-template-columns: repeat(3, 1fr); gap: 10px;">
                            <div class="stat-box"><div class="stat-lbl">H</div><div class="stat-val">\${H}</div></div>
                            <div class="stat-box"><div class="stat-lbl">L</div><div class="stat-val">\${L}</div></div>
                            <div class="stat-box"><div class="stat-lbl">L1</div><div class="stat-val">\${L1}</div></div>
                            <div class="stat-box"><div class="stat-lbl">A</div><div class="stat-val">\${A}</div></div>
                            <div class="stat-box"><div class="stat-lbl">H1</div><div class="stat-val">\${H1}</div></div>
                            <div class="stat-box"><div class="stat-lbl">J</div><div class="stat-val">\${J}</div></div>
                            <div class="stat-box"><div class="stat-lbl">H2</div><div class="stat-val">\${H2}</div></div>
                            <div class="stat-box"><div class="stat-lbl">S</div><div class="stat-val">\${S}</div></div>
                            <div class="stat-box"><div class="stat-lbl">B</div><div class="stat-val">\${B}</div></div>
                            <div class="stat-box"><div class="stat-lbl">N</div><div class="stat-val">\${N}</div></div>
                            <div class="stat-box"><div class="stat-lbl">N1</div><div class="stat-val">\${N1}</div></div>
                        </div>
                        <div class="tile-bolt"><i data-lucide="settings"></i> \${Bolt}</div>
                    </div>\`;
}).join('\n');

const path = 'e:\\\\PILLOW BLOCK WEB\\\\product-ucp.html';
let content = fs.readFileSync(path, 'utf8');

// Replace everything inside <div id="resultsGrid" class="tech-results-grid"> ... </div>
const startMarker = '<div id="resultsGrid" class="tech-results-grid">';
const endMarker = '</div>\\n        </div>\\n    </section>';

const startIndex = content.indexOf(startMarker) + startMarker.length;
const endIndex = content.lastIndexOf(endMarker);

if(startIndex !== -1 && endIndex !== -1) {
    const newContent = content.substring(0, startIndex) + '\\n' + htmlLines + '\\n            ' + content.substring(endIndex);
    fs.writeFileSync(path, newContent);
    console.log("Successfully rebuilt results HTML.");
} else {
    console.error("Could not find grid bounds.");
}
