package com.soc.java_sec_api.controller;

import com.soc.java_sec_api.model.ThreatLog;
import com.soc.java_sec_api.repository.ThreatLogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api/v1/threats") // Essa é a URL base da nossa API
public class ThreatLogController {

    @Autowired
    private ThreatLogRepository repository;

    // -------------------------------------------------------------------
    // GET: Retorna todos os logs (Vai alimentar o seu Dashboard Web no futuro)
    // URL: http://localhost:8080/api/v1/threats
    // -------------------------------------------------------------------
    @GetMapping
    public List<ThreatLog> listarAmeacas() {
        return repository.findAll(); // Faz o SELECT * automático no SQLite
    }

    // -------------------------------------------------------------------
    // POST: Recebe um novo ataque do script Python e salva no banco
    // URL: http://localhost:8080/api/v1/threats
    // -------------------------------------------------------------------
    @PostMapping
    public ResponseEntity<ThreatLog> registrarAmeaca(@RequestBody ThreatLog novoLog) {
        // O Spring pega o JSON do Python, converte para o objeto ThreatLog,
        // salva no banco via Hibernate e devolve o status 200 (OK).
        ThreatLog logSalvo = repository.save(novoLog);
        return ResponseEntity.ok(logSalvo);
    }
}