import pandas as pd
import os
import subprocess
from datetime import datetime

# Set paths
DOCX_PATH = "010test.docx"
OUTPUT_DIR = "/home/nothing/Python/tools"
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "library.pdf")

def convert_using_libreoffice():
    # Create tracking DataFrame
    log_df = pd.DataFrame({
        'source': [DOCX_PATH],
        'destination': [OUTPUT_PDF],
        'timestamp': [datetime.now()],
        'status': ['pending']
    })
    
    try:
        # LibreOffice conversion command
        cmd = ['libreoffice', '--headless', '--convert-to', 'pdf', 
               '--outdir', OUTPUT_DIR, DOCX_PATH]
        
        # Execute conversion
        process = subprocess.run(cmd, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE)
        
        if process.returncode == 0:
            log_df.loc[0, 'status'] = 'success'
        else:
            log_df.loc[0, 'status'] = f'failed: {process.stderr.decode()}'
            
    except Exception as e:
        log_df.loc[0, 'status'] = f'failed: {str(e)}'
    
    return log_df

# Run conversion
result = convert_using_libreoffice()
print(result.to_string())