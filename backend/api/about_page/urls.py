# ==========================================
"""
ABOUT ALL ROUTES
"""
# ==========================================
from django.urls import path
from api.about_page.views.about_page import (
    AboutTopBarView,
    SecureFutureTopBarView,
    SecureFutureItemView,
    SecurityFirmView,
    DigitalSecuritySolutionTopBarView,
    DigitalSecuritySolutionItemView,
    HappyJourneyTopBarView,
    HappyJourneyItemView,
)

urlpatterns = [
    path(
        'top-bar/',
        AboutTopBarView.as_view(),
        name='about_top_bar',
    ),
    path(
        'secure-future-top-bar/',
        SecureFutureTopBarView.as_view(),
        name='about_secure_futurea_top_bar',
    ),
    path(
        'secure-future-item/',
        SecureFutureItemView.as_view(),
        name='about_secure_future_item_view',
    ),
    path(
        'security-firm/',
        SecurityFirmView.as_view(),
        name='about_security_firm_view',
    ),
    path(
        'digital-security-solution-top-bar/',
        DigitalSecuritySolutionTopBarView.as_view(),
        name='about_digital_security_solution_top_bar',
    ),
    path(
        'digital-security-solution-item/',
        DigitalSecuritySolutionItemView.as_view(),
        name='about_digital_security_solution_item',
    ),
    path(
        'happy-journey/',
        HappyJourneyTopBarView.as_view(),
        name='about_happy_journey_top_bar',
    ),
    path(
        'happy-journey-item/',
        HappyJourneyItemView.as_view(),
        name='about_happy_journey_item',
    ),
]
