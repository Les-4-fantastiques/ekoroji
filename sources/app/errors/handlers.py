from flask import Blueprint, render_template

# création du Blueprint pour les erreurs
errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def error_404(error):
    """
    Gère l'erreur 404 (page non trouvée) et affiche la page correspondante.

    Args:
        error: L'objet d'erreur Flask qui a déclenché la fonction.

    Returns:
        Un tuple contenant la page d'erreur 404 et le code d'état HTTP 404.
    """
    return render_template('errors/404.html'), 404

@errors_bp.app_errorhandler(403)
def error_403(error):
    """
    Gère l'erreur 403 (accès refusé) et affiche la page correspondante.

    Args:
        error: L'objet d'erreur Flask qui a déclenché la fonction.

    Returns:
        Un tuple contenant la page d'erreur 403 et le code d'état HTTP 403.
    """
    return render_template('errors/403.html'), 403

@errors_bp.app_errorhandler(500)
def error_500(error):
    """
    Gère l'erreur 500 (erreur interne du serveur) et affiche la page correspondante.

    Args:
        error: L'objet d'erreur Flask qui a déclenché la fonction.

    Returns:
        Un tuple contenant la page d'erreur 500 et le code d'état HTTP 500.
    """
    return render_template('errors/500.html'), 500