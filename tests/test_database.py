import json
import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from services.database import Database


def test_spara_och_ladda_data(tmp_path):
    db_file = tmp_path / "db.json"
    db = Database(filename=db_file)
    db.spara_resultat("test@example.com", 12345)

    db2 = Database(filename=db_file)
    assert len(db2.historik) == 1
    assert db2.historik[0]["Email"] == "test@example.com"
    assert db2.historik[0]["Resultat"] == 12345


def test_tom_eller_korrupt_fil(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{fel JSON}")  # ogiltig JSON
    db = Database(filename=bad_file)
    assert db.historik == []
