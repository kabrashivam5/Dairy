from waitress import serve
import Dairy
serve(Dairy.app, host='0.0.0.0', port=8000)