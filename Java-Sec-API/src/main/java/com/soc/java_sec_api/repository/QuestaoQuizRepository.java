package com.soc.java_sec_api.repository;

import com.soc.java_sec_api.model.QuestaoQuiz;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface QuestaoQuizRepository extends JpaRepository<QuestaoQuiz, Integer> {
    
    // O Spring cria o SELECT automático filtrando as questões por módulo!
    List<QuestaoQuiz> findByModuloId(Integer moduloId);
}