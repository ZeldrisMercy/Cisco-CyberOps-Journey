package com.soc.java_sec_api.controller;

import com.soc.java_sec_api.model.QuestaoQuiz;
import com.soc.java_sec_api.repository.QuestaoQuizRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/quiz") // Nova rota principal
public class QuizController {

    @Autowired
    private QuestaoQuizRepository repository;

    // Rota 1: Traz TODAS as questões do banco
    // URL: http://localhost:8080/api/v1/quiz/questoes
    @GetMapping("/questoes")
    public List<QuestaoQuiz> listarTodasQuestoes() {
        return repository.findAll();
    }

    // Rota 2: Traz as questões de um módulo ESPECÍFICO (ex: módulo 5 de Redes)
    // URL: http://localhost:8080/api/v1/quiz/questoes/modulo/5
    @GetMapping("/questoes/modulo/{id}")
    public List<QuestaoQuiz> listarPorModulo(@PathVariable Integer id) {
        return repository.findByModuloId(id);
    }
}