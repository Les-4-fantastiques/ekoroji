import os


class HtmlToFlaskConverter:
    """
    A class to convert HTML and CSS files to a Flask application.

    Attributes:
    -----------
    html_files : list
        List of paths to HTML files to convert
    css_files : list
        List of paths to CSS files to convert
    output_file : str
        Path to output file for the generated Flask application
    """

    def __init__(self, html_files, css_files, output_file):
        """
        Initializes the HtmlToFlaskConverter object with HTML files, CSS files, and output file.

        Parameters:
        -----------
        html_files : list
            List of paths to HTML files to convert
        css_files : list
            List of paths to CSS files to convert
        output_file : str
            Path to output file for the generated Flask application
        """
        self.html_files = html_files
        self.css_files = css_files
        self.output_file = output_file

    def generate_flask_app(self):
        """
        Converts the HTML and CSS files to a Flask application and writes it to the output file.
        """
        # Create a Flask app object
        app = Flask(__name__)

        # Loop through all the HTML files and register them as Flask routes
        for html_file in self.html_files:
            # Open the HTML file and read its contents
            with open(html_file, 'r') as f:
                html_content = f.read()

            # Register the HTML file contents as a Flask route
            @app.route('/{}'.format(os.path.basename(html_file)))
            def render_html():
                return html_content

        # Loop through all the CSS files and add their contents to the Flask app's static files
        for css_file in self.css_files:
            # Open the CSS file and read its contents
            with open(css_file, 'r') as f:
                css_content = f.read()

            # Write the CSS file contents to a temporary file
            tmp_css_file = os.path.join(os.path.dirname(__file__), 'tmp.css')
            with open(tmp_css_file, 'w') as f:
                f.write(css_content)

            # Add the temporary CSS file to the Flask app's static files
            app.static_folder = os.path.dirname(tmp_css_file)
            app.static_url_path = '/static/{}'.format(os.path.basename(css_file))
            app.add_url_rule('/static/{}'.format(os.path.basename(css_file)), endpoint='static', view_func=app.send_static_file)

        # Write the generated Flask application to the output file
        with open(self.output_file, 'w') as f:
            f.write(app.__module__)

HtmlToFlaskConverter(['website/index.html', 'website/explorer.html', 'website/messcans.html'], ['website/styleexplorer.css', 'website/styleindex.css', 'website/stylemesscans.css'], "EkorojiGPT")