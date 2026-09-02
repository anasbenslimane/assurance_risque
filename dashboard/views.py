from django.db.models import Avg
from .decorators import agent_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import pandas as pd



from .forms import PredictionForm
from .predictor import model
from .models import PredictionHistory


def home(request):
    return render(request, "dashboard/home.html")

def login_view(request):

    # Si l'utilisateur est déjà connecté
    if request.user.is_authenticated:

        # Administrateur
        if request.user.is_superuser:
            return redirect("/admin/")

        # Agent
        if request.user.groups.filter(name="Agent").exists():
            return redirect("dashboard")

        return redirect("/")

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Connexion
            login(request, user)

            # Administrateur
            if user.is_superuser:
                return redirect("/admin/")

            # Agent Assurance
            if user.groups.filter(name="Agent").exists():
                return redirect("dashboard")

            # Utilisateur non autorisé
            logout(request)
            error = "Votre compte n'est pas autorisé à accéder à cette plateforme."

        else:
            error = "Nom d'utilisateur ou mot de passe incorrect."

    return render(
        request,
        "dashboard/login.html",
        {
            "error": error
        }
    )

@agent_required
def dashboard(request):

    # Historique des prédictions
    total_predictions = PredictionHistory.objects.count()

    total_claim = PredictionHistory.objects.filter(
        prediction="Claim"
    ).count()

    total_no_claim = PredictionHistory.objects.filter(
        prediction="No Claim"
    ).count()

    latest_predictions = PredictionHistory.objects.order_by(
        "-created_at"
    )[:5]

    if total_predictions > 0:
        avg_risk = round(
            PredictionHistory.objects.aggregate(
                Avg("claim_probability")
            )["claim_probability__avg"],
            1
        )
    else:
        avg_risk = 0

    # =========================
    # KPI Assurance (dataset)
    # =========================

    df = pd.read_csv("data/processed/insurance_clean.csv")

    total_contracts = len(df)

    claim_rate = round(df["HasClaim"].mean() * 100, 2)

    total_claim_amount = df["ClaimAmountTotal"].fillna(0).sum()

    avg_claim_amount = (
        df[df["ClaimAmountTotal"].notna()]["ClaimAmountTotal"].mean()
    )

    context = {

        # Historique plateforme
        "total_predictions": total_predictions,
        "total_claim": total_claim,
        "total_no_claim": total_no_claim,
        "avg_risk": avg_risk,
        "latest_predictions": latest_predictions,

        # KPI Assurance
        "total_contracts": total_contracts,
        "claim_rate": claim_rate,
        "total_claim_amount": round(total_claim_amount),
        "avg_claim_amount": round(avg_claim_amount),

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )

@agent_required
def analysis(request):

    df = pd.read_csv("data/processed/insurance_clean.csv")

    # =========================
    # Création des groupes
    # =========================

    df["AgeGroup"] = pd.cut(
        df["DrivAge"],
        bins=[18, 25, 35, 50, 100],
        labels=["18-25", "26-35", "36-50", "51+"]
    )

    df["BonusGroup"] = pd.cut(
        df["BonusMalus"],
        bins=[0, 75, 100, 150, 230],
        labels=["0-75", "76-100", "101-150", "151-230"]
    )

    df["VehAgeGroup"] = pd.cut(
        df["VehAge"],
        bins=[0, 2, 5, 10, 100],
        labels=["0-2", "3-5", "6-10", "11+"]
    )

    # =========================
    # Graphique 1 : Risque par âge
    # =========================

    age_risk = (
        df.groupby("AgeGroup", observed=False)["HasClaim"]
        .mean()
        .mul(100)
        .round(2)
    )

    # =========================
    # Graphique 2 : Bonus-Malus
    # =========================

    bonus_risk = (
        df.groupby("BonusGroup", observed=False)["HasClaim"]
        .mean()
        .mul(100)
        .round(2)
    )

    # =========================
    # Graphique 3 : Carburant
    # =========================

    fuel_counts = df["VehGas"].value_counts()

    # =========================
    # Graphique 4 : Régions
    # =========================

    region_risk = (
        df.groupby("Region")["HasClaim"]
        .mean()
        .mul(100)
        .round(2)
        .sort_values(ascending=False)
        .head(10)
    )

    # =========================
    # Graphique 5 : Âge du véhicule
    # =========================

    vehage_risk = (
        df.groupby("VehAgeGroup", observed=False)["HasClaim"]
        .mean()
        .mul(100)
        .round(2)
    )

    # =========================
    # Graphique 6 : Marques
    # =========================

    brand_counts = df["VehBrand"].value_counts().head(11)

    # =========================
    # Graphique 7 : Puissance
    # =========================

    power_risk = (
        df.groupby("VehPower")["HasClaim"]
        .mean()
        .mul(100)
        .round(2)
        .sort_index()
    )

    # =========================
    # Graphique 8 : Claim vs No Claim
    # =========================

    claim_counts = df["HasClaim"].value_counts().sort_index()

    # =========================
    # KPI
    # =========================

    total_contracts = int(len(df))
    claim_rate = round(float(df["HasClaim"].mean() * 100), 2)

    top_region = str(region_risk.index[0])
    top_region_rate = float(region_risk.iloc[0])

    top_fuel = str(fuel_counts.idxmax())
    top_fuel_count = int(fuel_counts.max())

    # =========================
    # Context
    # =========================

    context = {

        # KPI
        "total_contracts": total_contracts,
        "claim_rate": claim_rate,
        "top_region": top_region,
        "top_region_rate": top_region_rate,
        "top_fuel": top_fuel,
        "top_fuel_count": top_fuel_count,

        # Âge
        "age_labels": [str(x) for x in age_risk.index],
        "age_values": [float(x) for x in age_risk.values],

        # Bonus
        "bonus_labels": [str(x) for x in bonus_risk.index],
        "bonus_values": [float(x) for x in bonus_risk.values],

        # Carburant
        "fuel_labels": [str(x) for x in fuel_counts.index],
        "fuel_values": [int(x) for x in fuel_counts.values],

        # Régions
        "region_labels": [str(x) for x in region_risk.index],
        "region_values": [float(x) for x in region_risk.values],

        # Âge véhicule
        "vehage_labels": [str(x) for x in vehage_risk.index],
        "vehage_values": [float(x) for x in vehage_risk.values],

        # Marques
        "brand_labels": [str(x) for x in brand_counts.index],
        "brand_values": [int(x) for x in brand_counts.values],

        # Puissance
        "power_labels": [str(x) for x in power_risk.index],
        "power_values": [float(x) for x in power_risk.values],

        # Claim / No Claim
        "claim_labels": ["Sans sinistre", "Avec sinistre"],
        "claim_values": [int(x) for x in claim_counts.values],
    }

    return render(request, "dashboard/analysis.html", context)


@agent_required
def prediction(request):

    result = None

    if request.method == "POST":

        form = PredictionForm(request.POST)

        

        if form.is_valid():

            data = pd.DataFrame([form.cleaned_data])

            pred = model.predict(data)[0]
            proba = model.predict_proba(data)[0]

            # Probabilité de sinistre
            risk = proba[1] * 100

            # ---------- Niveau de risque ----------

            if risk < 30:
                level = "Faible"
                message = (
                    "Le modèle estime que ce contrat présente "
                    "un faible risque de sinistre."
                )

            elif risk < 60:
                level = "Moyen"
                message = (
                    "Le modèle estime que ce contrat présente "
                    "un risque moyen de sinistre."
                )

            else:
                level = "Élevé"
                message = (
                    "Le modèle estime que ce contrat présente "
                    "un risque élevé de sinistre."
                )

            # ---------- Résultat ----------

            result = {
                "prediction": "Claim" if pred == 1 else "No Claim",
                "claim_probability": round(risk, 2),
                "no_claim_probability": round(proba[0] * 100, 2),
                "risk_level": level,
                "message": message,
            }

            # ---------- Historique ----------

            PredictionHistory.objects.create(
                Exposure=form.cleaned_data["Exposure"],
                VehPower=form.cleaned_data["VehPower"],
                VehAge=form.cleaned_data["VehAge"],
                DrivAge=form.cleaned_data["DrivAge"],
                BonusMalus=form.cleaned_data["BonusMalus"],
                VehBrand=form.cleaned_data["VehBrand"],
                VehGas=form.cleaned_data["VehGas"],
                Area=form.cleaned_data["Area"],
                Density=form.cleaned_data["Density"],
                Region=form.cleaned_data["Region"],
                prediction=result["prediction"],
                claim_probability=result["claim_probability"],
                risk_level=result["risk_level"],
            )

            

        else:
            print("Erreurs du formulaire :", form.errors)

    else:
        form = PredictionForm()

    return render(
        request,
        "dashboard/prediction.html",
        {
            "form": form,
            "result": result,
        },
    )

@agent_required
def history(request):

    predictions = PredictionHistory.objects.order_by("-created_at")

    # Récupération des filtres
    risk = request.GET.get("risk", "")
    prediction = request.GET.get("prediction", "")
    brand = request.GET.get("brand", "")
    region = request.GET.get("region", "")
    date_from = request.GET.get("date_from", "")
    date_to = request.GET.get("date_to", "")

    # -----------------------------
    # Filtre niveau de risque
    # -----------------------------

    if risk:
        predictions = predictions.filter(
            risk_level=risk
        )

    # -----------------------------
    # Filtre décision
    # -----------------------------

    if prediction:
        predictions = predictions.filter(
            prediction=prediction
        )

    # -----------------------------
    # Filtre marque
    # -----------------------------

    if brand:
        predictions = predictions.filter(
            VehBrand=brand
        )

    # -----------------------------
    # Filtre région
    # -----------------------------

    if region:
        predictions = predictions.filter(
            Region=region
        )

    # -----------------------------
    # Filtre date de début
    # -----------------------------

    if date_from:
        predictions = predictions.filter(
            created_at__date__gte=date_from
        )

    # -----------------------------
    # Filtre date de fin
    # -----------------------------

    if date_to:
        predictions = predictions.filter(
            created_at__date__lte=date_to
        )

    # -----------------------------
    # Marques disponibles
    # -----------------------------

    brands = (
        PredictionHistory.objects
        .values_list("VehBrand", flat=True)
        .distinct()
        .order_by("VehBrand")
    )

    # -----------------------------
    # Régions disponibles
    # -----------------------------

    regions = (
        PredictionHistory.objects
        .values_list("Region", flat=True)
        .distinct()
        .order_by("Region")
    )

    # -----------------------------
    # Nombre de résultats
    # -----------------------------

    result_count = predictions.count()

    return render(
        request,
        "dashboard/history.html",
        {
            "predictions": predictions,

            # Filtres sélectionnés
            "selected_risk": risk,
            "selected_prediction": prediction,
            "selected_brand": brand,
            "selected_region": region,
            "selected_date_from": date_from,
            "selected_date_to": date_to,

            # Options
            "brands": brands,
            "regions": regions,

            # Compteur
            "result_count": result_count,
        },
    )