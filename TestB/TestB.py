import ProcessingToolboxB as pt # import functions for data processing

# Set initial data
result = {}
f = ".\17.12_evidence_data.json"

# Process file
with open(f) as file:
    for line in file:
        pt.processLine(result, line)

# Process data
NdRt = pt.NormalizeResult(result)
SrtRt = sorted(NdRt.items(), key=lambda e: e[0][1])

# Save result
pt.WriteResultAsCSV(SrtRt)
